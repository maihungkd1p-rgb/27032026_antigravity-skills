# Kiểm Chứng Claims → Verification

**Module:** Process  
**Mục đích:** Verify facts, claims, và thông tin trước khi publish content

## Khi Nào Dùng Module Này

**Load module này khi:**
- Content có số liệu quan trọng cần verify
- Claims mạnh/controversial về người, tổ chức, thương hiệu
- Quotes từ experts/executives cần xác nhận
- Nội dung nhạy cảm (legal, medical, financial)
- News/updates cần đảm bảo accuracy

**Không cần dùng khi:**
- Content opinion-based không có factual claims
- Storytelling chủ quan, personal experience
- General knowledge đã established

---

## Quy Trình Kiểm Chứng

### Bước 1: Identify Claims Cần Verify

**Phân loại theo risk level:**

#### 🔴 High Risk - BẮT BUỘC verify
- **Statistics & Numbers:** "90% doanh nghiệp Việt Nam sử dụng AI"
- **Attribution:** "CEO Google nói rằng..."
- **Legal/Regulatory:** "Luật mới quy định..."
- **Medical/Health:** "Nghiên cứu chứng minh X chữa Y"
- **Financial:** "Cổ phiếu tăng 300% trong quý"
- **Negative claims:** "Công ty X vi phạm..."

#### 🟡 Medium Risk - Nên verify
- **Dates & Events:** "Ra mắt vào tháng 11/2024"
- **Rankings:** "Top 3 startup VN theo..."
- **Comparisons:** "Nhanh hơn đối thủ 2x"
- **Industry trends:** "E-commerce tăng 40% YoY"

#### 🟢 Low Risk - Optional verify
- **General statements:** "AI đang phát triển nhanh"
- **Common knowledge:** "Hà Nội là thủ đô Việt Nam"
- **Opinions:** "Tôi nghĩ rằng..."

**Focus resources vào High → Medium → Low**

### Bước 2: Verification Methods

**5 phương pháp chính:**

#### Method 1: Source Check (Kiểm tra nguồn)

**Đối với statistics/facts:**
```
Claim: "35% doanh nghiệp VN dùng AI"

Verify:
1. Tìm nguồn gốc: Ai công bố? Khi nào?
2. Check credibility: Tổ chức uy tín? Methodology clear?
3. Context: Sample size? Định nghĩa "dùng AI"?
4. Recency: Còn relevant không?

Tools: web_search, web_fetch
Search: "[claim] source", "[claim] report", "[statistic] study"
```

**Red flags:**
- ❌ Không tìm thấy nguồn gốc
- ❌ Nguồn không uy tín (blog vô danh)
- ❌ Methodology không rõ
- ❌ Quá cũ (>2-3 năm cho trends)

#### Method 2: Cross-Reference (So sánh chéo)

**Đối với major claims:**
```
Claim: "Startup X raise $10M Series A"

Verify:
1. Tìm ít nhất 2-3 nguồn độc lập confirm
2. Check official announcement (company blog, press release)
3. Look for reputable news coverage

Sources to check:
- Company official channels
- Tech news sites (TechCrunch, VnExpress, etc.)
- Investment databases (Crunchbase)
- LinkedIn posts from founders/investors
```

**Confidence levels:**
- ✅ **High:** 3+ reputable sources confirm
- ⚠️ **Medium:** 1-2 sources, hoặc chỉ company announcement
- ❌ **Low:** Chỉ 1 source không uy tín, hoặc conflicting info

#### Method 3: Direct Verification (Xác minh trực tiếp)

**Đối với quotes/attributions:**
```
Claim: "CEO công ty X nói: '...'"

Verify:
1. Tìm quote trong context gốc (interview, speech, article)
2. Check chính xác wording (không paraphrase sai)
3. Verify context (quote có bị taken out of context?)

Tools:
- web_search: "[quote]" "[person name]"
- web_fetch: Đọc full article/interview
- Check official channels: Twitter, LinkedIn, company blog
```

**Đối với data points:**
```
Claim: "Doanh thu công ty Y là 100M USD"

Verify:
1. Tìm financial reports, earnings calls
2. Check official filings (if public company)
3. Look for audited numbers vs estimates

Sources:
- Company investor relations
- Financial databases
- Audited financial statements
```

#### Method 4: Logical Consistency Check

**Đối với claims khó verify trực tiếp:**

```
Claim: "App Z có 5 triệu users tại VN"

Consistency checks:
- Vietnam population: ~100M
  → 5M = 5% penetration, có reasonable không?
- Competitor numbers: App tương tự có bao nhiêu?
- Growth trajectory: Có match với reported growth không?
- Market size: Total addressable market có đủ lớn?
```

**Red flags:**
- Numbers quá cao/thấp so với benchmark
- Không consistent với other metrics
- Claims extraordinary nhưng không có evidence

#### Method 5: Temporal Verification (Kiểm tra thời điểm)

**Đối với time-sensitive info:**

```
Claim: "Sản phẩm ra mắt tháng 12/2024"

Verify:
1. Check announcement dates
2. Look for official launch info
3. Verify current status (đã launch hay còn upcoming?)

Important:
- Distinguish: announced vs launched
- Check for delays: Plan vs actual
- Current date: Monday, October 20, 2025
```

**Note thời điểm:**
- Past events: Có xảy ra đúng không?
- Future plans: Clarify đây là plan, không phải fact
- Present state: Check real-time status

### Bước 3: Handle Uncertainty

**Khi không verify được 100%:**

#### Option A: Hedge Language

**Từ mạnh → Từ nhẹ:**
```
❌ "90% doanh nghiệp dùng AI"
✅ "Theo báo cáo X, khoảng 90% doanh nghiệp được khảo sát cho biết đang dùng AI"

❌ "CEO nói rằng..."
✅ "Trong interview với Y, CEO chia sẻ rằng..."

❌ "Sản phẩm ra mắt tháng 12"
✅ "Công ty dự định ra mắt sản phẩm vào tháng 12"
```

#### Option B: Cite Source Explicitly

**Khi có nguồn nhưng không 100% confident:**
```
"Theo báo cáo của [Source], [claim]. Tuy nhiên, [note limitations]."

Ví dụ:
"Theo khảo sát của Công ty A với 500 doanh nghiệp tại TP.HCM, 
35% cho biết đang sử dụng AI trong marketing. Con số này có thể 
khác biệt với toàn quốc hoặc với doanh nghiệp quy mô khác."
```

#### Option C: Remove/Replace

**Khi không verify được và risk cao:**
```
- Bỏ claim đó hoàn toàn
- Thay bằng claim khác có thể verify
- Dùng general statement thay vì specific number
```

### Bước 4: Document Verification

**Tracking template:**

```markdown
## Verification Log

### Claim 1: [Statement]
- **Risk level:** High/Medium/Low
- **Method:** Source check / Cross-reference / Direct
- **Sources checked:**
  1. [Source 1] - [URL] - [Result]
  2. [Source 2] - [URL] - [Result]
- **Status:** ✅ Verified / ⚠️ Partially verified / ❌ Cannot verify
- **Action:** Keep as is / Hedge / Cite source / Remove
- **Final wording:** [Adjusted claim if needed]

### Claim 2: [Statement]
...
```

---

## Verification Checklist

**Pre-publish checklist cho content:**

### Statistics & Numbers
- [ ] Có source rõ ràng?
- [ ] Source credible?
- [ ] Recency OK? (<2 years for trends)
- [ ] Context đầy đủ? (sample size, methodology)
- [ ] Cross-checked với 2+ sources?

### Quotes & Attributions
- [ ] Found original source?
- [ ] Wording chính xác?
- [ ] Context preserved?
- [ ] Person/title đúng?

### Claims về Companies/Products
- [ ] Verified từ official channels?
- [ ] Dates/numbers accurate?
- [ ] Status current? (nếu là present tense)

### Negative/Controversial Claims
- [ ] **Extra careful verification**
- [ ] Multiple sources confirm?
- [ ] Legal review needed?
- [ ] Consider defamation risk?

### Vietnam-Specific Info
- [ ] Sources relevant to VN context?
- [ ] Not just translating global data?
- [ ] Local examples verified?

---

## Ví Dụ Thực Tế

### Case 1: Verify Startup Funding

**Original claim:**
```
"Startup fintech Momo vừa nhận được 100 triệu USD vòng Series C 
từ quỹ đầu tư ABC vào tháng 9/2024."
```

**Verification process:**

**Step 1 - Identify risk:** 🔴 High (specific number, date, names)

**Step 2 - Method:** Cross-reference + Direct verification

**Step 3 - Search:**
```
web_search("Momo Series C funding 2024")
web_search("Momo ABC fund investment")
web_fetch([Relevant news articles])
```

**Step 4 - Findings:**
- ✅ TechCrunch: Confirms $100M Series C
- ✅ VnExpress: Confirms September 2024
- ⚠️ Investor name: Found "ABC Capital" not "ABC fund"
- ✅ Official Momo blog: Press release confirms

**Step 5 - Verification result:**
- Amount: ✅ Verified
- Timing: ✅ Verified  
- Investor name: ⚠️ Need correction
- Round: ✅ Verified

**Step 6 - Final wording:**
```
"Startup fintech Momo vừa nhận được 100 triệu USD vòng Series C 
từ ABC Capital vào tháng 9/2024, theo thông báo chính thức của công ty."
```

**Verification log:**
```
Claim: Momo Series C $100M from ABC fund
Risk: High
Sources:
1. TechCrunch article (Sept 15, 2024) - Confirmed
2. Momo official blog - Confirmed  
3. VnExpress (Sept 16, 2024) - Confirmed
Status: ✅ Verified (with correction)
Action: Fixed investor name "ABC fund" → "ABC Capital"
```

---

### Case 2: Verify Statistics

**Original claim:**
```
"85% người Việt Nam sử dụng smartphone, cao nhất Đông Nam Á."
```

**Verification process:**

**Step 1 - Identify risk:** 🔴 High (specific %, comparative claim)

**Step 2 - Method:** Source check + Cross-reference

**Step 3 - Search:**
```
web_search("Vietnam smartphone penetration rate 2024")
web_search("Southeast Asia smartphone usage statistics")
web_fetch([Reports from We Are Social, GSMA, etc.])
```

**Step 4 - Findings:**
- Report "Digital 2024 Vietnam" (We Are Social): 82.5% smartphone penetration
- GSMA Intelligence: Vietnam 80.1%, Singapore 87.2%, Malaysia 84.1%
- Different reports = slightly different numbers
- Vietnam NOT highest in SEA (Singapore higher)

**Step 5 - Verification result:**
- Percentage: ⚠️ Close but not exact (82-85% range)
- Highest in SEA: ❌ Incorrect (Singapore higher)

**Step 6 - Final wording:**
```
"Hơn 80% người Việt Nam sử dụng smartphone (theo báo cáo Digital 2024), 
nằm trong nhóm các nước có tỷ lệ cao nhất Đông Nam Á."
```

**Verification log:**
```
Claim: 85% smartphone usage, highest in SEA
Risk: High
Sources:
1. We Are Social Digital 2024 - 82.5%
2. GSMA Intelligence - 80.1%
3. Various sources show Singapore ~87%
Status: ⚠️ Partially verified, needs correction
Action: Adjusted to "Hơn 80%" + removed "highest" claim
```

---

### Case 3: Verify Quote

**Original claim:**
```
"Bill Gates từng nói: 'AI sẽ thay đổi mọi ngành nghề trong 5 năm tới.'"
```

**Verification process:**

**Step 1 - Identify risk:** 🔴 High (attribution to famous person)

**Step 2 - Method:** Direct verification

**Step 3 - Search:**
```
web_search("Bill Gates AI change every industry 5 years")
web_search("Bill Gates AI quote 2024")
```

**Step 4 - Findings:**
- ❌ Cannot find exact quote with these words
- ✅ Found similar sentiment in 2023 interview: "AI will transform most jobs"
- Context: He said "within a decade" not "5 years"
- No exact match for the quoted wording

**Step 5 - Verification result:**
- Quote accuracy: ❌ Not exact wording
- Attribution: ⚠️ Sentiment similar but paraphrased incorrectly
- Context: ❌ Timeline wrong

**Step 6 - Options:**

**Option A - Remove quote:**
```
"Theo nhiều chuyên gia công nghệ, AI được dự đoán sẽ thay đổi 
đáng kể nhiều ngành nghề trong thập kỷ tới."
```

**Option B - Fix với proper attribution:**
```
"Bill Gates từng chia sẻ trong interview năm 2023 rằng AI sẽ 
transform hầu hết các công việc trong vòng một thập kỷ."
```

**Verification log:**
```
Claim: Bill Gates quote about AI
Risk: High
Sources:
1. Multiple searches - no exact match
2. 2023 interview - similar sentiment, different wording
Status: ❌ Cannot verify exact quote
Action: Removed specific quote, used general statement
```

---

## Red Flags - Cảnh Báo

**Dừng ngay và double-check khi thấy:**

### 🚩 Source Red Flags
- Source không có tên tác giả
- Website không rõ credentials
- Thông tin từ "according to research" mà không cite cụ thể
- Blog cá nhân không uy tín
- Social media rumors

### 🚩 Content Red Flags
- Numbers quá tròn, quá đẹp (100%, 10x, etc.)
- Claims extraordinary (too good to be true)
- Contradicts common knowledge
- Lacks specific details (vague statements)
- Sensationalist language

### 🚩 Context Red Flags
- Quote taken out of context
- Cherry-picked data (chọn lọc numbers favorable)
- Outdated info presented as current
- Mixing correlation với causation
- Comparing apples to oranges

**Khi thấy red flags → Verify extra careful hoặc remove claim**

---

## Tools & Resources

### Primary Tools
- **web_search:** Tìm multiple sources
- **web_fetch:** Đọc chi tiết articles/reports
- **google_drive_search:** Check internal docs (nếu có)

### Credible Sources (Vietnam)
- **Government:** gso.gov.vn (General Statistics Office)
- **News:** VnExpress, Tuổi Trẻ, Thanh Niên (established media)
- **Tech:** VietnamInsider, Tech in Asia Vietnam
- **Business:** Vietstock, CafeF (financial data)
- **Reports:** We Are Social, GSMA, McKinsey Vietnam

### International Sources
- Official websites (.gov, .edu, .org)
- Reuters, AP, Bloomberg (wire services)
- Academic journals (peer-reviewed)
- Industry reports (Gartner, IDC, McKinsey)
- Company official channels

### Fact-Checking Sites
- Snopes.com (general)
- FactCheck.org
- PolitiFact (political claims)
- Google Fact Check Explorer

---

## Output Format

**Verification summary cho writer:**

```markdown
## Verified Content: [Topic]

### Claims Status

✅ **Verified & Safe to Use:**
1. [Claim 1] - [Source]
2. [Claim 2] - [Source]

⚠️ **Use with Caution (với disclaimer):**
1. [Claim 3] - [Why caution + how to phrase]

❌ **Cannot Verify - Do Not Use:**
1. [Claim 4] - [Why removed]

### Recommended Wording Adjustments

Original: [...]
Adjusted: [...]
Reason: [...]

### Sources to Cite

1. [Source name] - [URL] - [What it verifies]
2. [Source name] - [URL] - [What it verifies]

### Notes for Writer
- [Any additional context]
- [Limitations to mention]
- [Disclaimers to include]
```

---

## Best Practices

### 1. Verify Before Writing
Tốt nhất là verify trong research phase, không phải sau khi viết xong

### 2. Err on Side of Caution
Khi không chắc → Hedge hoặc remove (đừng risk reputation)

### 3. Cite Strong Sources
Transparent about sources tăng credibility

### 4. Update Regularly
Re-verify time-sensitive claims nếu content publish sau nhiều ngày

### 5. Document Everything
Lưu verification log để reference sau này

---

## Integration với Workflow

**Vị trí trong flow:**

```
User request
  ↓
Research/Analysis (nghien-cuu.md hoặc phan-tich.md)
  ↓
DRAFT content
  ↓
kiem-chung.md ← Verify claims trong draft
  ↓
Adjust wording based on verification
  ↓
quy-tac-viet.md (Vietnamese rules)
  ↓
Final content
```

**Hoặc:**

```
Research phase
  ↓
kiem-chung.md ← Verify research findings trước khi viết
  ↓
Write content với verified info
  ↓
Output module
```

---

**Token budget:** ~2,000 tokens  
**Priority:** HIGH for sensitive/important content  
**Impact:** Protect reputation, avoid misinformation  
**Note:** Better to remove claim than publish unverified info
