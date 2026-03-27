---
name: planning
description: Use when you have a spec or requirements for a multi-step task, before touching code or analyzing data.
---

# Writing Plans

## Overview

Write comprehensive implementation plans assuming the executor has zero context. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

**Announce at start:** "I'm using the planning skill to create the implementation plan."

**Save plans to:** `docs/plans/YYYY-MM-DD-<topic>.md` (create directory if needed)

## Bite-Sized Task Granularity

**Each step is one action (2-5 minutes):**
- "Write the failing test" - step
- "Run it to make sure it fails" - step
- "Implement the minimal code to make the test pass" - step
- "Run the tests and make sure they pass" - step
- "Commit" - step

## Plan Document Header

**Every plan MUST start with this header:**

```markdown
# [Feature/Topic Name] Implementation Plan

**Goal:** [One sentence describing what this builds/analyzes]

**Strategy/Architecture:** [2-3 sentences about approach]

**Tech Stack/Tools:** [Key technologies, libraries, or data sources]

---
```

## Task Structure

```markdown
### Task N: [Component/Step Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: Write the failing test / Prepare analysis**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

**Step 2: Run test to verify it fails / Verify data source**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

**Step 3: Write minimal implementation / Perform analysis**

```python
def function(input):
    return expected
```

**Step 4: Run test to verify it passes / Verify results**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

**Step 5: Commit / Save Output**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
```

## Remember
- Exact file paths always
- Complete code/steps in plan
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
