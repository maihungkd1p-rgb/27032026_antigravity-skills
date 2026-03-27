# RAG Skill Examples

## Example 1: Mat Bang Knowledge (Thực tế)

**Input:** 9 chapters from "Đến Sahara Mở Quán Trà Đá" (27 documents, PDF/DOCX)

**Output:**
```
matbang_kinh_doanh/
├── metadata.json (22 artifacts, cross-refs)
└── artifacts/
    ├── overview.md            (3KB)
    ├── qa_pairs.md            (3KB) ← Q&A format
    ├── Chuong_I_A_BaiHocATM.md    (2.4KB) ← Split from 29KB
    ├── Chuong_I_B_NguoiThayYana.md (2.3KB)
    ├── Chuong_I_C_TamQuanTrong.md  (2.2KB)
    ├── Chuong_III_A-D_*.md    (2-5KB) ← Split from 40KB
    ├── Chuong_IX_A-C_*.md     (2.6-3.4KB) ← Split from 28KB
    └── [Original chapters preserved]
```

**Result:** 91% RAG score ✅

---

## Example 2: Contract Templates

**Input:** 3 hợp đồng mẫu (DOCX)

**Output:**
```
matbang_hop_dong/
├── metadata.json
└── artifacts/
    ├── hop_dong_thue_nha_dat.md
    ├── hop_dong_gop_von.md
    └── hop_dong_xay_dung_cua_hang.md
```

**Key learnings:**
- Hợp đồng cần giữ nguyên format, không split
- Có thể extract key terms vào Q&A pairs

---

## Chunking Decision Tree

```
File size?
├── < 8KB: Keep as-is ✓
├── 8-15KB: Consider splitting if has multiple topics
└── > 15KB: MUST split
    ├── Has clear chapters? → Split by chapter
    ├── Has topic clusters? → Split by topic
    └── Long narrative? → Split at natural breaks (~4KB each)
```
