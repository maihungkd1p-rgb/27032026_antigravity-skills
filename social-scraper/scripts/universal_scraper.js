const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const USER_DATA_DIR = path.resolve(__dirname, '../../../browser_data');

async function main() {
    const url = process.argv[2];
    if (!url) {
        console.error('Please provide a URL. Usage: node universal_scraper.js <url>');
        process.exit(1);
    }

    console.log(`Launching browser... Target: ${url}`);

    // Launch with persistent context to save login state
    const context = await chromium.launchPersistentContext(USER_DATA_DIR, {
        headless: false,
        viewport: { width: 1280, height: 800 },
        slowMo: 100, // Slower actions to appear more human-like
        args: [
            '--disable-notifications',
            '--disable-blink-features=AutomationControlled' // Helps evade some detection
        ]
    });

    // Add init script to mask webdriver
    await context.addInitScript(() => {
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined,
        });
    });

    const page = await context.newPage();

    // Set a realistic User-Agent (optional, but good practice)
    await page.setExtraHTTPHeaders({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    });

    try {
        console.log('Navigating...');
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
        await page.waitForTimeout(3000); // Initial wait
        console.log('Page loaded.');

        let results = [];

        if (url.includes('facebook.com')) {
            console.log('Strategy: Facebook');
            results = await scrapeFacebook(page);
        } else if (url.includes('reddit.com')) {
            console.log('Strategy: Reddit');
            results = await scrapeReddit(page);
        } else if (url.includes('tiktok.com')) {
            console.log('Strategy: TikTok');
            results = await scrapeTikTok(page);
        } else {
            console.log('Strategy: Generic');
            results = await scrapeGeneric(page);
        }

        console.log('--- RESULTS ---');
        console.log(JSON.stringify(results, null, 2));

        // Save to file in proper location
        const resultPath = path.resolve(process.cwd(), 'scrape_results.json');
        fs.writeFileSync(resultPath, JSON.stringify(results, null, 2));
        console.log(`Saved results to ${resultPath}`);

    } catch (error) {
        console.error('An error occurred:', error);
    } finally {
        console.log('Closing in 5 seconds...');
        await new Promise(r => setTimeout(r, 5000));
        await context.close();
    }
}

async function scrapeFacebook(page) {
    if (await page.isVisible('input[name="email"]') || await page.isVisible('div[aria-label="Accessible login button"]')) {
        console.log('⚠️  LOGIN REQUIRED! Please log in manually.');
        await page.waitForTimeout(60000);
    }

    // Auto-scroll
    for (let i = 0; i < 5; i++) {
        await page.mouse.wheel(0, 1000);
        await page.waitForTimeout(1000);
    }

    const postSelector = 'div[role="article"], div[data-pagelet*="FeedUnit"], div.x1yztbdb.x1n2onr6.h676nmdw';
    try {
        await page.waitForSelector(postSelector, { timeout: 15000 });
    } catch (e) {
        console.log('Main selector timeout. Dumping page title to debug...');
        console.log('Page Title:', await page.title());
    }

    // Wait for redirects or dynamic content settling
    console.log('Waiting 10s for page to settle...');
    await page.waitForTimeout(10000);

    let posts = await page.$$(postSelector);
    if (posts.length === 0) {
        console.log('Retry with broader selector...');
        // Try finding feed first
        const feed = await page.$('div[role="feed"]');
        if (feed) {
            posts = await feed.$$(':scope > div');
        }
    }

    // If still no posts, try nuclear text dump of main area
    if (posts.length === 0) {
        console.log('Selectors failed. Attempting text dump of main content...');
        const main = await page.$('div[role="main"]');
        if (main) {
            const text = await main.innerText();
            // Split by double newlines as a poor-man's post separator
            const chunks = text.split('\n\n').filter(t => t.length > 50).slice(0, 15);
            return chunks.map((c, i) => ({
                rank: i + 1,
                content: c,
                link: page.url()
            }));
        }
    }

    console.log(`Found ${posts.length} potential posts.`);

    let results = await extractTop3(posts, async (post) => {
        const text = await post.innerText().catch(() => '');
        // Heuristic link extraction
        const link = await post.evaluate(el => {
            const anchors = Array.from(el.querySelectorAll('a'));
            // Priority: Permalinks -> Videos -> Any link
            const specificLink = anchors.find(a =>
                (a.href.includes('/posts/') || a.href.includes('/permalink/') || a.href.includes('/groups/')) &&
                !a.href.includes('/user/')
            );
            return specificLink ? specificLink.href : anchors[0]?.href;
        }).catch(() => null);

        return { content: text.split('\n').slice(0, 5).join('\n'), link: link };
    });

    // If extraction yielded nothing (e.g. empty containers), try nuclear text dump
    if (results.length === 0) {
        console.log('Extraction yielded 0 results. Attempting text dump of main content...');
        const main = await page.$('div[role="main"]');
        if (main) {
            const text = await main.innerText();
            const chunks = text.split('\n\n').filter(t => t.length > 50).slice(0, 15);
            results = chunks.map((c, i) => ({
                rank: i + 1,
                content: c,
                link: page.url()
            }));
        }
    }

    return results;
}

async function scrapeReddit(page) {
    // Reddit uses 'shreddit-post' tag in modern UI or distinct divs
    const selector = 'shreddit-post, div.Post';
    await page.waitForSelector(selector, { timeout: 10000 }).catch(() => console.log('Timeout waiting for Reddit posts'));

    const posts = await page.$$(selector);
    return await extractTop3(posts, async (post) => {
        const title = await post.getAttribute('post-title') || await post.evaluate(el => el.querySelector('h3')?.innerText);
        const permalink = await post.getAttribute('permalink') || await post.getAttribute('content-href');
        return {
            title: title || 'No Title',
            link: permalink ? (permalink.startsWith('http') ? permalink : `https://www.reddit.com${permalink}`) : 'No Link'
        };
    });
}

async function scrapeTikTok(page) {
    if (await page.isVisible('button[data-e2e="login-button"]')) {
        console.log('⚠️ TikTok might ask for login/captcha. Resolve it manually if needed.');
        await page.waitForTimeout(10000);
    }

    // TikTok generic feed item selector
    const selector = 'div[data-e2e="user-post-item"], div[class*="DivItemContainer"]';
    await page.waitForSelector(selector, { timeout: 10000 }).catch(() => console.log('Timeout waiting for TikTok posts'));

    const posts = await page.$$(selector);
    return await extractTop3(posts, async (post) => {
        const desc = await post.evaluate(el => el.innerText); // TikTok descriptions are usually short
        const link = await post.evaluate(el => el.querySelector('a')?.href);
        return {
            description: desc.split('\n')[0],
            link: link || 'No Link'
        };
    });
}

async function scrapeGeneric(page) {
    let articles = await page.$$('article');
    if (articles.length === 0) {
        const headings = await page.$$('h1, h2, h3');
        const parents = [];
        for (const h of headings) {
            const parent = await h.evaluateHandle(el => el.closest('div, section, li') || el.parentElement);
            if (parent.asElement()) parents.push(parent.asElement());
        }
        articles = parents.slice(0, 10);
    }

    return await extractTop3(articles, async (el) => {
        const title = await el.evaluate(node => {
            const h = node.querySelector('h1, h2, h3, h4');
            return h ? h.innerText : node.innerText.slice(0, 50);
        });
        const link = await el.evaluate(node => node.querySelector('a')?.href);
        return { title: title ? title.trim().replace(/\n/g, ' ') : 'No Title', link: link || page.url() };
    });
}

// Helper to limit to top 15 and format
async function extractTop3(elements, extractorFn) {
    const results = [];
    for (let i = 0; i < Math.min(elements.length, 15); i++) {
        try {
            const data = await extractorFn(elements[i]);
            if (data && (data.content || data.title || data.description)) {
                results.push({ rank: i + 1, ...data });
            }
        } catch (e) {
            console.error(`Error extracting item ${i}:`, e);
        }
    }
    return results;
}

main();
