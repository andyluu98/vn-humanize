# -*- coding: utf-8 -*-
"""Quét nhanh dấu vết AI dạng chữ trong văn bản tiếng Việt.

Cách dùng:
    python quet-dau-vet.py <file.txt|file.md>
    python quet-dau-vet.py - < file.txt          (đọc từ stdin)

Chỉ bắt dấu vết về chữ (từ sáo, gạch dài, emoji, lời chatbot, mở bài khuôn).
Dấu vết về cấu trúc (bộ ba, câu chốt, văn dịch) vẫn phải đọc bằng mắt.
"""
import re
import sys
import unicodedata

# (mã mẫu, tên, danh sách cụm). So khớp không phân biệt hoa thường.
NHOM = [
    ("1", "Không chỉ... mà còn", [
        r"không chỉ\b.{0,80}?\bmà còn", r"không đơn thuần là\b.{0,80}?\bmà là",
        r"không phải là\b.{0,60}?\bmà là"]),
    ("2", "Câu chốt kịch tính", [
        "đó chính là chìa khóa", "điều này thay đổi tất cả", "hãy suy ngẫm",
        "điều này cho thấy tầm quan trọng"]),
    ("3", "Câu nghe sâu sắc", [
        "suy cho cùng", "xét cho cùng", "về bản chất", "điều thực sự quan trọng",
        "cốt lõi của vấn đề", "dầu mỏ mới"]),
    ("4", "Dẫn dắt dài", [
        "hãy cùng tìm hiểu", "cùng khám phá", "trong bài viết này", "dưới đây là",
        "có thể nói rằng", "không thể phủ nhận", "điều đáng chú ý là", "nói một cách thẳng thắn"]),
    ("5", "Cãi với người không tồn tại", [
        "nhiều người lầm tưởng", "bạn có thể nghĩ rằng", "đừng hiểu lầm", "cần nói rõ là"]),
    ("6", "Mở bài, kết bài khuôn", [
        "trong thời đại 4.0", "trong thời đại công nghệ", "kỷ nguyên số", "trong bối cảnh",
        "ngày càng phát triển", "tương lai đầy hứa hẹn", "tương lai tươi sáng"]),
    ("9", "Từ nối đầu câu", [
        r"(?:^|[.!?]\s+)(?:ngoài ra|bên cạnh đó|hơn nữa|đồng thời|không những thế)\b",
        r"(?:^|[.!?]\s+)(?:thứ nhất|thứ hai|thứ ba|cuối cùng),"]),
    ("13", "Từ sáo quen mặt", [
        "đóng vai trò then chốt", "đóng vai trò quan trọng", "bức tranh toàn cảnh", "hành trình",
        "không ngừng", "vượt trội", "tối ưu hóa", "khai phá", "nâng tầm", "chìa khóa", "đòn bẩy",
        "bệ phóng", "lan tỏa", "giá trị cốt lõi", "toàn diện", "sâu sắc", "mạnh mẽ", "đột phá",
        "kiến tạo", "đồng hành", "liền mạch", "hệ sinh thái", "cuộc cách mạng", "mở ra cánh cửa",
        "tiềm năng to lớn", "vô vàn", "muôn màu", "tất yếu"]),
    ("14", "Thổi phồng ý nghĩa", [
        "đánh dấu bước ngoặt", "bước ngoặt", "kỷ nguyên mới", "dấu ấn sâu đậm", "minh chứng cho",
        "khẳng định vị thế"]),
    ("16", "Đuôi câu nối thêm", [
        r",\s*qua đó\b", r",\s*từ đó giúp\b", r",\s*góp phần\b"]),
    ("17", "Giọng quảng cáo", [
        "tọa lạc", "điểm đến không thể bỏ qua", "đẳng cấp", "hàng đầu", "trải nghiệm tuyệt vời",
        "hoàn hảo"]),
    ("18", "Uy tín không tên", [
        "các chuyên gia cho rằng", "nhiều chuyên gia", "nhiều nghiên cứu chỉ ra",
        "giới phân tích"]),
    ("19", "Né là, có", ["đóng vai trò là", "được xem như là", "sở hữu", "mang đến"]),
    ("23", "Lời chatbot", [
        "chắc chắn rồi", "câu hỏi rất hay", "hy vọng thông tin này", "hy vọng bài viết",
        "bạn có muốn tôi", "hãy cho tôi biết", "tuyệt vời!"]),
    ("24", "Giới hạn hiểu biết", [
        "tính đến thời điểm", "dựa trên thông tin hiện có", "chưa có nhiều thông tin"]),
    ("V2", "Việc, sự, một cách", [r"\bmột cách\b", r"\bviệc\b", r"\bsự\b"]),
    ("V3", "Hán Việt trang trọng", [
        "tiến hành", "thực hiện", "triển khai", "hiện thực hóa", "nhằm mục đích", "mang tính"]),
]

# Mẫu V2 chỉ báo khi mật độ cao, vì "việc", "sự" vẫn là từ thường.
NGUONG_MAT_DO = {"V2": 3.0}  # số lần trên 100 chữ

GACH = {"\u2014": "gạch dài", "\u2013": "gạch vừa"}
NGOAC_CONG = "“”‘’"


def la_emoji(ch):
    return unicodedata.category(ch) == "So" and ord(ch) > 0x2000


def tieu_de_viet_hoa(dong):
    m = re.match(r"\s*#+\s+(.*)", dong)
    if not m:
        return False
    chu = [w for w in re.findall(r"\w+", m.group(1)) if w.isalpha()]
    return len(chu) >= 3 and all(w[0].isupper() for w in chu)


def quet(van_ban):
    dong = van_ban.splitlines()
    so_chu = max(len(re.findall(r"\w+", van_ban)), 1)
    ket_qua = []  # (mã, tên, số lần, [số dòng])
    thap = van_ban.lower()
    for ma, ten, cum in NHOM:
        vi_tri = []
        for c in cum:
            mau = c if any(k in c for k in r"\.?()[]^") else re.escape(c)
            for m in re.finditer(mau, thap, flags=re.MULTILINE):
                # Lấy dòng theo cuối cụm: mẫu từ nối bắt cả dấu chấm của câu trước
                vi_tri.append(thap.count("\n", 0, m.end() - 1) + 1)
        if not vi_tri:
            continue
        mat_do = len(vi_tri) * 100 / so_chu
        if ma in NGUONG_MAT_DO and mat_do < NGUONG_MAT_DO[ma]:
            continue
        ket_qua.append((ma, ten, len(vi_tri), sorted(set(vi_tri))))

    for ky, ten in GACH.items():
        vt = [i for i, d in enumerate(dong, 1) if ky in d]
        if vt:
            ket_qua.append(("10", ten, sum(d.count(ky) for d in dong), vt))
    vt = [i for i, d in enumerate(dong, 1) if any(la_emoji(ch) for ch in d)]
    if vt:
        ket_qua.append(("21", "emoji", len(vt), vt))
    vt = [i for i, d in enumerate(dong, 1) if tieu_de_viet_hoa(d)]
    if vt:
        ket_qua.append(("21", "tiêu đề viết hoa mọi chữ", len(vt), vt))
    vt = [i for i, d in enumerate(dong, 1) if re.match(r"\s*[-*]\s+\*\*[^*]+:\*\*", d)]
    if len(vt) >= 3:
        ket_qua.append(("20", "danh sách có nhãn in đậm", len(vt), vt))
    vt = [i for i, d in enumerate(dong, 1) if any(ch in d for ch in NGOAC_CONG)]
    if vt:
        ket_qua.append(("22", "ngoặc kép cong (yếu)", len(vt), vt))
    return so_chu, ket_qua


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "-":
        van_ban = sys.stdin.read()
    else:
        with open(sys.argv[1], encoding="utf-8") as f:
            van_ban = f.read()
    so_chu, ket_qua = quet(van_ban)
    tong = sum(k[2] for k in ket_qua)
    print(f"Số chữ: {so_chu}. Dấu vết dạng chữ: {tong} ({tong * 100 / so_chu:.1f} trên 100 chữ)")
    for ma, ten, n, vt in sorted(ket_qua, key=lambda k: -k[2]):
        dong = ", ".join(map(str, vt[:12])) + (" ..." if len(vt) > 12 else "")
        print(f"  [mẫu {ma:>3}] {ten}: {n} lần, dòng {dong}")
    if not ket_qua:
        print("  Không thấy dấu vết dạng chữ. Vẫn cần đọc để soát cấu trúc.")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
