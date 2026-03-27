import os

base_dir = r"C:\Users\maihu\.gemini\antigravity\knowledge\matbang_kinh_doanh\artifacts"
output_file = r"C:\Users\maihu\.gemini\antigravity\global_skills\rag\temp_knowledge_dump.txt"

files = [
    "Chuong_I_A_BaiHocATM.md", "Chuong_I_B_NguoiThayYana.md", "Chuong_I_C_TamQuanTrong.md",
    "Chương II  - Đến Sahara Mở Quán Trà Đá.md",
    "Chuong_III_A_ThiTruong.md", "Chuong_III_B_ChucNang.md", "Chuong_III_C_TiepCan.md", "Chuong_III_D_TongKet6T.md",
    "Chương IV  - Đến Sahara Mở Quán Trà Đá.md",
    "Chương V  - Đến Sahara Mở Quán Trà Đá.md",
    "Chương VI  - Đến Sahara Mở Quán Trà Đá.md",
    "Chương VII  - Đến Sahara Mở Quán Trà Đá.md",
    "Chương VIII  - Đến Sahara Mở Quán Trà Đá.md",
    "Chuong_IX_A_DieuKhoanHopDong.md", "Chuong_IX_B_ChienThuatDamPhan.md", "Chuong_IX_C_KyKetCongChung.md",
    "qa_pairs.md"
]

with open(output_file, 'w', encoding='utf-8') as outfile:
    # Add title
    outfile.write("# KIẾN THỨC KINH DOANH MẶT BẰNG (FULL)\n\n")
    
    for fname in files:
        fpath = os.path.join(base_dir, fname)
        if os.path.exists(fpath):
            outfile.write(f"\n\n--- SOURCE START: {fname} ---\n\n")
            try:
                with open(fpath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
            except Exception as e:
                outfile.write(f"Error reading file: {e}")
            outfile.write(f"\n\n--- SOURCE END: {fname} ---\n\n")
        else:
            print(f"Missing file: {fname}")

print(f"Successfully concatenated knowledge to {output_file}")
