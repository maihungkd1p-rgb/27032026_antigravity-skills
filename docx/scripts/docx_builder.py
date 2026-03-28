"""
DocxBuilder — Corporate Word Document Wrapper (Antigravity V4)
Applies 4-Layer UX: Structure → Information → Visuals → Interaction.
"""
import os
from datetime import datetime
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


class DocxStyles:
    """Corporate color palette and font constants."""
    DARK_BLUE = RGBColor(0, 51, 102)
    MEDIUM_BLUE = RGBColor(0, 81, 152)
    GRAY = RGBColor(128, 128, 128)
    LIGHT_GRAY = RGBColor(200, 200, 200)
    FONT_BODY = 'Arial'
    FONT_SIZE_BODY = Pt(11)
    FONT_SIZE_H1 = Pt(16)
    FONT_SIZE_H2 = Pt(14)
    FONT_SIZE_TITLE = Pt(24)
    FONT_SIZE_SMALL = Pt(9)
    TABLE_STYLE = 'Medium Shading 1 Accent 1'


class DocxBuilder:
    """
    Fluent API wrapper for python-docx.
    Every method returns `self` to enable chaining:
        DocxBuilder("Title").add_heading("Ch1").add_paragraph("text").save(path)
    """

    def __init__(self, title: str):
        self.doc = Document()
        self.title = title
        self._setup_styles()
        self._add_title(title)

    def _setup_styles(self):
        """Initialize corporate font/color defaults."""
        styles = self.doc.styles

        # Normal style
        normal = styles['Normal']
        normal.font.name = DocxStyles.FONT_BODY
        normal.font.size = DocxStyles.FONT_SIZE_BODY

        # Title style
        if 'Title' in styles:
            ts = styles['Title']
            ts.font.name = DocxStyles.FONT_BODY
            ts.font.size = DocxStyles.FONT_SIZE_TITLE
            ts.font.bold = True
            ts.font.color.rgb = DocxStyles.DARK_BLUE

        # Heading 1
        if 'Heading 1' in styles:
            h1 = styles['Heading 1']
            h1.font.name = DocxStyles.FONT_BODY
            h1.font.size = DocxStyles.FONT_SIZE_H1
            h1.font.bold = True
            h1.font.color.rgb = DocxStyles.DARK_BLUE

        # Heading 2
        if 'Heading 2' in styles:
            h2 = styles['Heading 2']
            h2.font.name = DocxStyles.FONT_BODY
            h2.font.size = DocxStyles.FONT_SIZE_H2
            h2.font.bold = True
            h2.font.color.rgb = DocxStyles.MEDIUM_BLUE

    def _add_title(self, text: str):
        """Add centered document title (internal, called once in __init__)."""
        p = self.doc.add_paragraph(text, style='Title')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Structure Layer ──────────────────────────────────────

    def add_toc_placeholder(self):
        """Add a TOC placeholder that prompts user to generate real TOC in Word."""
        p = self.doc.add_paragraph()
        run = p.add_run("[MỤC LỤC — Nhấn chuột phải → Update Field sau khi mở Word]")
        run.font.italic = True
        run.font.color.rgb = DocxStyles.GRAY
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self.add_page_break()
        return self

    def add_heading(self, text: str, level: int = 1):
        """Add a heading at the specified level (1-3)."""
        self.doc.add_heading(text, level=level)
        return self

    def add_page_break(self):
        """Insert a page break between major sections."""
        self.doc.add_page_break()
        return self

    # ── Information Layer ────────────────────────────────────

    def add_paragraph(self, text: str, bold: bool = False, italic: bool = False):
        """Add a body text paragraph with optional formatting."""
        p = self.doc.add_paragraph()
        run = p.add_run(text)
        if bold:
            run.bold = True
        if italic:
            run.italic = True
        return self

    def add_bullet_list(self, items: list):
        """Add a bulleted list to break up long text blocks."""
        for item in items:
            self.doc.add_paragraph(str(item), style='List Bullet')
        return self

    def add_numbered_list(self, items: list):
        """Add a numbered list for sequential procedures."""
        for item in items:
            self.doc.add_paragraph(str(item), style='List Number')
        return self

    def add_table(self, headers: list, data: list):
        """Add a data table with styled header row."""
        table = self.doc.add_table(rows=1, cols=len(headers))
        table.style = DocxStyles.TABLE_STYLE

        # Header row
        for i, h in enumerate(headers):
            cell = table.rows[0].cells[i]
            cell.text = str(h)
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.bold = True

        # Data rows
        for row_data in data:
            row_cells = table.add_row().cells
            for i, val in enumerate(row_data):
                row_cells[i].text = str(val)
        return self

    # ── Visual Layer ─────────────────────────────────────────

    def add_source_note(self, source: str, date: str = None):
        """Add a small italic source annotation at the current position."""
        if date is None:
            date = datetime.now().strftime("%d/%m/%Y")
        p = self.doc.add_paragraph()
        run = p.add_run(f"Nguồn: {source} | Ngày tạo: {date}")
        run.font.size = DocxStyles.FONT_SIZE_SMALL
        run.font.italic = True
        run.font.color.rgb = DocxStyles.GRAY
        return self

    # ── Interaction Layer ────────────────────────────────────

    def add_hyperlink(self, paragraph_text: str, url: str, link_text: str = None):
        """Add a paragraph containing a clickable hyperlink."""
        p = self.doc.add_paragraph()
        if paragraph_text:
            p.add_run(paragraph_text)

        # Build hyperlink XML element
        part = p.part
        r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
        hyperlink = OxmlElement('w:hyperlink')
        hyperlink.set(qn('r:id'), r_id)
        new_run = OxmlElement('w:r')
        rPr = OxmlElement('w:rPr')
        c = OxmlElement('w:color')
        c.set(qn('w:val'), '0563C1')
        rPr.append(c)
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)
        new_run.append(rPr)
        t = OxmlElement('w:t')
        t.text = link_text or url
        new_run.append(t)
        hyperlink.append(new_run)
        p._element.append(hyperlink)
        return self

    def add_footer_page_numbers(self):
        """Add 'Trang X / Y' footer to the default section."""
        section = self.doc.sections[-1]
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # "Trang "
        run1 = p.add_run("Trang ")
        run1.font.size = DocxStyles.FONT_SIZE_SMALL
        run1.font.color.rgb = DocxStyles.GRAY

        # PAGE field
        fld_page = OxmlElement('w:fldSimple')
        fld_page.set(qn('w:instr'), 'PAGE')
        run_page = OxmlElement('w:r')
        rPr_page = OxmlElement('w:rPr')
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), '18')  # 9pt
        rPr_page.append(sz)
        run_page.append(rPr_page)
        t_page = OxmlElement('w:t')
        t_page.text = '1'
        run_page.append(t_page)
        fld_page.append(run_page)
        p._element.append(fld_page)

        # " / "
        run2 = p.add_run(" / ")
        run2.font.size = DocxStyles.FONT_SIZE_SMALL
        run2.font.color.rgb = DocxStyles.GRAY

        # NUMPAGES field
        fld_total = OxmlElement('w:fldSimple')
        fld_total.set(qn('w:instr'), 'NUMPAGES')
        run_total = OxmlElement('w:r')
        rPr_total = OxmlElement('w:rPr')
        sz2 = OxmlElement('w:sz')
        sz2.set(qn('w:val'), '18')
        rPr_total.append(sz2)
        run_total.append(rPr_total)
        t_total = OxmlElement('w:t')
        t_total.text = '1'
        run_total.append(t_total)
        fld_total.append(run_total)
        p._element.append(fld_total)
        return self

    # ── Save ─────────────────────────────────────────────────

    def save(self, filepath: str):
        """Save the document. Creates parent directories if needed."""
        # Safe path handling — avoid crash on bare filename
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
        self.doc.save(filepath)
        print(f"✅ Đã lưu file Word thành công tại: {filepath}")
        return self


# ── Usage Example ────────────────────────────────────────────
if __name__ == "__main__":
    (
        DocxBuilder("Báo Cáo Tình Hình Kinh Doanh Q1/2026")
        .add_footer_page_numbers()
        .add_toc_placeholder()
        .add_heading("1. Executive Summary", level=1)
        .add_paragraph("Quý 1 chứng kiến sự tăng trưởng vượt bậc 15% so với cùng kỳ.", bold=True)
        .add_bullet_list([
            "Doanh thu đạt 120 tỷ VNĐ.",
            "Chi phí marketing tối ưu giảm 5%.",
            "Mở mới 3 cửa hàng tại khu vực miền Nam."
        ])
        .add_page_break()
        .add_heading("2. Chỉ Số Tài Chính", level=1)
        .add_table(
            ["Khu vực", "Doanh thu (Tỷ)", "Tăng trưởng", "Đánh giá"],
            [
                ["Miền Bắc", "65", "+10%", "Hoàn thành"],
                ["Miền Trung", "20", "+5%", "Chậm tiến độ"],
                ["Miền Nam", "35", "+25%", "Vượt chỉ tiêu"],
            ]
        )
        .add_source_note("Hệ thống POS Anna Eyewear")
        .add_hyperlink("Xem chi tiết: ", "https://example.com/report", "Báo cáo đầy đủ")
        .save("03_Outputs/Bao_Cao_Q1_2026_Sample.docx")
    )
