---
name: deployment-guard
description: Pre-deployment validation checks. Use when the user asks to deploy, release, or push to production. Ensures code quality gates are passed before deployment.
---

# Deployment Guard

## When to use this skill
- User says "deploy", "release", "push to production", or "go live"
- User asks to verify code before merging to main/master
- User wants a pre-flight check before CI/CD

## Workflow Checklist

Copy and update this checklist during execution:

```markdown
## Pre-Deployment Checklist
- [ ] Lint check passed
- [ ] Type check passed (if applicable)
- [ ] Unit tests passed
- [ ] Build successful
- [ ] No uncommitted changes
- [ ] Branch is up-to-date with target
```

## Validation Steps

### Step 1: Check Git Status
```bash
git status --porcelain
```
- If output is not empty, STOP and warn about uncommitted changes.

### Step 2: Run Linter
Detect project type and run appropriate linter:

| Project Type | Command |
|--------------|---------|
| Node.js | `npm run lint` or `npx eslint .` |
| Python | `ruff check .` or `flake8` |
| Go | `go vet ./...` |

### Step 3: Run Type Checks (if applicable)
| Project Type | Command |
|--------------|---------|
| TypeScript | `npx tsc --noEmit` |
| Python | `mypy .` (if configured) |

### Step 4: Run Tests
```bash
# Node.js
npm test

# Python
pytest

# Go
go test ./...
```

### Step 5: Build
```bash
# Node.js
npm run build

# Python (if applicable)
python -m build
```

### Step 6: Branch Sync Check
```bash
git fetch origin
git log HEAD..origin/main --oneline
```
- If commits exist, warn that local branch is behind.

## Decision Gate

After all checks:
- **All passed**: Proceed with deployment or notify user it's safe
- **Any failed**: List failures and recommend fixes before proceeding

## Bypass Flag
If user explicitly says "force deploy" or "skip checks", log a warning but proceed. Never auto-approve bypasses.
