# -*- coding: utf-8 -*-
"""Soát văn phong: đếm các mẫu dấu vết có tên trong văn bản tiếng Việt.

Cách dùng:
    python quet-dau-vet.py <file|-> [--json] [--nguong N]

    <file|->     file .txt hoặc .md; dùng "-" để đọc từ stdin
    --json       in kết quả dạng JSON
    --nguong N   ngưỡng mật độ, tính bằng số lần trên 1000 chữ (mặc định 15)

Mã thoát: 1 khi mật độ vượt ngưỡng, 0 khi không vượt.

Đây không phải máy dò AI. Công cụ chỉ đếm các mẫu có tên trong
references/cac-mau-dau-vet-ai.md (mã 1-43, V1-V8) và không ước lượng ai viết.
Khối code và code trong dòng được bỏ qua. Dấu vết về cấu trúc (bộ ba, câu chốt,
văn dịch) vẫn phải đọc bằng mắt.
"""
import argparse
import json
import re
import sys
import unicodedata

NGUONG_MAC_DINH = 15.0
CUA_SO = 300  # ngân sách tính trên mỗi 300 chữ
GHI_CHU = ("Ghi chú: đây là bộ soát văn phong, chỉ đếm các mẫu có tên trong danh mục. "
           "Nó không đoán văn bản do người hay máy viết. Kết quả thấp vẫn cần đọc lại bằng mắt.")

TU = re.compile(r"\w+")
# Viết bằng chr() để mã nguồn không chứa ký tự gạch dài, gạch vừa.
GACH_DAI, GACH_VUA, BA_CHAM = chr(0x2014), chr(0x2013), chr(0x2026)


def R(mau):
    return re.compile(mau, re.MULTILINE)


DAU_CAU = r"(?:^|[.!?]\s+)"
NHOM_NGUOI = (r"(?:doanh nghiệp|tập đoàn|công ty|startup|học sinh|sinh viên|người|cá nhân|"
              r"nhân viên|lãnh đạo|giáo viên|trẻ em|gia đình|hộ kinh doanh|cửa hàng|chuyên gia)")

# (mã, tên, cụm, ngân sách). Cụm là chuỗi (khớp nguyên từ, không phân biệt hoa thường)
# hoặc regex đã biên dịch chạy trên chữ thường. Ngân sách là số lần được phép trên
# 300 chữ; None nghĩa là gặp là báo.
NHOM = [
    ("1", "Không chỉ... mà còn", [
        R(r"không chỉ\b.{0,80}?\bmà còn"), R(r"không đơn thuần là\b.{0,80}?\bmà là"),
        R(r"không phải là\b.{0,60}?\bmà là")], None),
    ("2", "Câu chốt kịch tính", [
        "đó chính là chìa khóa", "điều này thay đổi tất cả", "hãy suy ngẫm",
        "điều này cho thấy tầm quan trọng"], None),
    ("3", "Câu nghe sâu sắc", [
        "suy cho cùng", "xét cho cùng", "về bản chất", "điều thực sự quan trọng",
        "cốt lõi của vấn đề", "dầu mỏ mới"], None),
    ("4", "Dẫn dắt dài", [
        "hãy cùng tìm hiểu", "cùng khám phá", "trong bài viết này", "dưới đây là",
        "có thể nói rằng", "không thể phủ nhận", "điều đáng chú ý là",
        "nói một cách thẳng thắn"], None),
    ("5", "Cãi với người không tồn tại", [
        "nhiều người lầm tưởng", "bạn có thể nghĩ rằng", "đừng hiểu lầm", "cần nói rõ là"], None),
    ("6", "Mở bài, kết bài khuôn", [
        "trong thời đại 4.0", "trong thời đại công nghệ", "kỷ nguyên số", "trong bối cảnh",
        "ngày càng phát triển", "tương lai đầy hứa hẹn", "tương lai tươi sáng",
        R(DAU_CAU + r"(?:tóm lại|nhìn chung),")], None),
    ("9", "Từ nối đầu câu dày", [
        R(DAU_CAU + r"(?:ngoài ra|bên cạnh đó|hơn nữa|đồng thời|không những thế|đặc biệt|"
          r"tuy nhiên)\b"),
        R(DAU_CAU + r"(?:thứ nhất|thứ hai|thứ ba|cuối cùng),")], 2),
    ("13", "Từ sáo quen mặt", [
        "đóng vai trò then chốt", "đóng vai trò quan trọng", "bức tranh toàn cảnh", "hành trình",
        "không ngừng", "vượt trội", "tối ưu hóa", "khai phá", "nâng tầm", "chìa khóa", "đòn bẩy",
        "bệ phóng", "lan tỏa", "giá trị cốt lõi", "toàn diện", "sâu sắc", "mạnh mẽ", "đột phá",
        "kiến tạo", "đồng hành", "liền mạch", "hệ sinh thái", "cuộc cách mạng", "mở ra cánh cửa",
        "tiềm năng to lớn", "vô vàn", "muôn màu", "tất yếu"], None),
    ("14", "Thổi phồng ý nghĩa", [
        "đánh dấu bước ngoặt", "bước ngoặt", "kỷ nguyên mới", "dấu ấn sâu đậm", "minh chứng cho",
        "khẳng định vị thế"], None),
    ("15", "Liên hệ mơ hồ", [
        "liên quan đến", "liên quan tới", "gắn liền với", "gắn bó với",
        "có mối liên hệ mật thiết"], 1),
    ("16", "Đuôi câu nối thêm", [
        R(r",\s*qua đó\b"), R(r",\s*từ đó giúp\b"), R(r",\s*góp phần\b")], None),
    ("17", "Giọng quảng cáo", [
        "tọa lạc", "điểm đến không thể bỏ qua", "đẳng cấp", "hàng đầu", "trải nghiệm tuyệt vời",
        "hoàn hảo"], None),
    ("18", "Uy tín không tên", [
        "các chuyên gia cho rằng", "nhiều chuyên gia", "nhiều nghiên cứu chỉ ra",
        "giới phân tích"], None),
    ("19", "Né là, có", ["đóng vai trò là", "được xem như là", "sở hữu", "mang đến"], None),
    ("23", "Lời chatbot", [
        "chắc chắn rồi", "câu hỏi rất hay", "hy vọng thông tin này", "hy vọng bài viết",
        "bạn có muốn tôi", "hãy cho tôi biết", "tuyệt vời!"], None),
    ("24", "Giới hạn hiểu biết", [
        "tính đến thời điểm", "dựa trên thông tin hiện có", "chưa có nhiều thông tin"], None),
    ("30", "Liệt kê phủ định", [
        R(r"không phải[^.!?\n]{0,60}[.!?]\s+không phải"),
        R(r"không phải[^.!?\n]{1,40},\s*(?:cũng\s+)?không phải")], None),
    ("31", "Vật vô tri làm việc của người", [
        "con số biết nói", "dữ liệu lên tiếng", "số liệu nói lên", "con số nói lên",
        "con số không biết nói dối"], None),
    ("34", "Phạm vi giả từ... đến...", [
        R(rf"(?<!\w)từ (?:các |những )?{NHOM_NGUOI}[^.,;:!?\n]{{0,30}}? (?:đến|tới) "
          rf"(?:các |những )?{NHOM_NGUOI}(?!\w)")], 1),
    ("35", "Câu gói ý lặp", ["điều này có nghĩa là", "nói cách khác", "tức là"], 2),
    ("36", "Cân bằng hai phía", [
        "đều có ưu và nhược điểm", "có ưu và nhược điểm riêng", "con dao hai lưỡi",
        "tùy thuộc vào nhiều yếu tố", "vừa là cơ hội vừa là thách thức"], None),
    ("37", "Định lượng mơ hồ", [
        "nhiều nghiên cứu", "phần lớn", "hầu hết", "đáng kể", "được đánh giá cao", "rộng rãi"], 2),
    ("42", "Hạn chế chung chung", [
        "cần nghiên cứu thêm", "cần có thêm nghiên cứu", "cần thêm nghiên cứu",
        "cần được nghiên cứu thêm"], None),
    ("V2", "Việc, sự, một cách", [
        R(r"\bmột cách\b"), R(r"(?<!công )(?<!làm )\bviệc\b"),
        R(r"\bsự\b(?! (?:kiện|cố|thật))")], 9),
    ("V3", "Hán Việt trang trọng", [
        "tiến hành", "thực hiện", "triển khai", "hiện thực hóa", "nhằm mục đích", "mang tính"], None),
    ("V8", "Từ thừa nghĩa", [
        "hoàn toàn đầy đủ", "tái lập lại", "quay trở lại", "cùng chung", "đang trong quá trình",
        "các những", "bổ sung thêm"], None),
]

# Mẫu 28: cụm ngắn rồi hai chấm ở đầu câu, kiểu "Kết quả: ...", "Bí quyết: ...".
DAU_LAT = (r"(?:điều|điểm|cái|bí quyết|kết quả|sự thật|vấn đề|lý do|câu trả lời|mấu chốt|"
           r"bài học|thực tế|tin vui|tin buồn|kết luận|nói gọn|nói ngắn gọn|quan trọng nhất|"
           r"hay nhất|bất ngờ|nghịch lý)")
HAI_CHAM = R(rf"(?:^|(?<=[.!?] ))[ \t]*{DAU_LAT}(?:[ \t]+[^\s:.,!?]+){{0,4}}[ \t]*:[ \t]+\S")
# Mẫu 29: câu hỏi ngắn có từ để hỏi, ngay sau là câu trả lời.
CAU_TRONG_DONG = re.compile(r"[^.!?\n]+[.!?]+")
TU_HOI = re.compile(r"(?<!\w)(?:tại sao|vì sao|sao lại|kết quả|lý do|bí quyết|điều gì|là gì|"
                    r"thế nào|ra sao|thì sao)(?!\w)")
CUM_TU_HOI = re.compile(r"(?<!\w)(?:bạn có biết|vậy điều gì)(?!\w)")
MO_DE = re.compile(r"(?:theo yêu cầu|đề bài|\S+(?:\s+\S+){0,4}\s+là (?:từ )?viết tắt)")
CHO_TRONG = [
    re.compile(r"\[(?:tên|chèn|điền|ngày|số|địa chỉ|họ tên|link|thêm|nội dung|insert|name|your)"
               r"[^\]\n]{0,40}\]", re.I),
    re.compile(r"\[\s*(?:\.\.\.|" + BA_CHAM + r")\s*\]"),
    re.compile(r"(?<!\w)XX+(?:[.,]X+)*\s?%"),
    re.compile(r"(?<!\w)XX/XX(?:/XXXX)?(?!\w)"),
]
GACH = re.compile(f"{GACH_DAI}|(?<!\\d){GACH_VUA}|{GACH_VUA}(?!\\d)")  # bỏ qua khoảng số 2020-2025
NGOAC_CONG_KEP = chr(0x201C) + chr(0x201D)


def bien_dich(cum):
    if isinstance(cum, re.Pattern):
        return cum
    return re.compile(r"(?<!\w)" + re.escape(cum) + r"(?!\w)")


NHOM = [(ma, ten, [bien_dich(c) for c in cum], ns) for ma, ten, cum, ns in NHOM]


def so_dong(van_ban, vi_tri):
    return van_ban.count("\n", 0, vi_tri) + 1


def bo_code(van_ban):
    """Xóa khối code và code trong dòng, giữ nguyên số dòng."""
    ra, rao = [], None
    for dong in van_ban.splitlines():
        m = re.match(r"\s*(`{3,}|~{3,})", dong)
        if m and (rao is None or m.group(1)[0] == rao):
            rao = None if rao else m.group(1)[0]
            ra.append("")
        else:
            ra.append("" if rao else re.sub(r"`[^`\n]*`", " ", dong))
    return "\n".join(ra)


def vuot_ngan_sach(so_lan, ngan_sach, so_chu):
    if ngan_sach is None:
        return so_lan > 0
    return so_lan > ngan_sach * max(1.0, so_chu / CUA_SO)


def quet_nhom(thap, so_chu):
    ket_qua = []
    for ma, ten, mau, ngan_sach in NHOM:
        # Lấy dòng theo cuối cụm: mẫu từ nối bắt cả dấu chấm của câu trước
        vt = [so_dong(thap, m.end() - 1) for p in mau for m in p.finditer(thap)]
        if vuot_ngan_sach(len(vt), ngan_sach, so_chu):
            ket_qua.append((ma, ten, len(vt), sorted(set(vt))))
    return ket_qua


def kiem_tu_hoi(thap):
    vt = [so_dong(thap, m.start()) for m in CUM_TU_HOI.finditer(thap)]
    for i, dong in enumerate(thap.splitlines(), 1):
        cau = [c.strip() for c in CAU_TRONG_DONG.findall(dong)]
        for hoi, dap in zip(cau, cau[1:]):
            if (hoi.endswith("?") and not dap.endswith("?")
                    and len(TU.findall(hoi)) <= 6 and TU_HOI.search(hoi)):
                vt.append(i)
    return vt


def kiem_mo_de(thap):
    for i, dong in enumerate(thap.splitlines(), 1):
        d = dong.strip().lstrip("#").strip()
        if d:
            return [i] if MO_DE.match(d) else []
    return []


def la_emoji(ch):
    return unicodedata.category(ch) == "So" and ord(ch) > 0x2000


def tieu_de_viet_hoa(dong):
    m = re.match(r"\s*#+\s+(.*)", dong)
    if not m:
        return False
    chu = [w for w in TU.findall(m.group(1)) if w.isalpha()]
    return len(chu) >= 3 and all(w[0].isupper() for w in chu)


def theo_dong(dong, dieu_kien):
    return [i for i, d in enumerate(dong, 1) if dieu_kien(d)]


def quet_dac_biet(sach, thap, so_chu):
    dong = sach.splitlines()
    ket_qua = []

    def them(ma, ten, vt, n=None):
        if vt:
            ket_qua.append((ma, ten, n if n is not None else len(vt), sorted(set(vt))))

    vt = [so_dong(sach, m.start()) for m in GACH.finditer(sach)]
    if vuot_ngan_sach(len(vt), 1, so_chu):
        them("10", "gạch dài, gạch vừa dày", vt)
    them("21", "emoji", theo_dong(dong, lambda d: any(la_emoji(c) for c in d)))
    them("21", "tiêu đề viết hoa mọi chữ", theo_dong(dong, tieu_de_viet_hoa))
    vt = theo_dong(dong, lambda d: re.match(r"\s*[-*]\s+\*\*[^*]+:\*\*", d))
    if len(vt) >= 3:
        them("20", "danh sách có nhãn in đậm", vt)
    if '"' in sach and any(c in sach for c in NGOAC_CONG_KEP):
        them("22", "trộn ngoặc kép cong và thẳng",
             theo_dong(dong, lambda d: any(c in d for c in NGOAC_CONG_KEP)), 1)
    them("28", "Hai chấm lật bài", [so_dong(thap, m.start()) for m in HAI_CHAM.finditer(thap)])
    them("29", "Tự hỏi tự trả lời", kiem_tu_hoi(thap))
    them("38", "Mở bằng nhắc đề, định nghĩa", kiem_mo_de(thap))
    them("39", "Chỗ trống mẫu", [so_dong(sach, m.start()) for p in CHO_TRONG
                                 for m in p.finditer(sach)])
    return ket_qua


def tach_cau(sach):
    """Trả về [(số dòng, số chữ)] cho từng câu; bỏ tiêu đề markdown."""
    cau = []
    for i, dong in enumerate(sach.splitlines(), 1):
        dong = dong.strip()
        if not dong or dong.startswith("#"):
            continue
        dong = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", dong)
        for c in re.split(r"(?<=[.!?" + BA_CHAM + r"])\s+", dong):
            n = len(TU.findall(c))
            if n:
                cau.append((i, n))
    return cau


def chuoi_deu(cau, lech=3, toi_thieu=3):
    """Các chuỗi >= 3 câu liền nhau có độ dài chênh nhau không quá 3 chữ."""
    ra, hien = [], []
    for dong, n in cau:
        do_dai = [x for _, x in hien] + [n]
        if hien and max(do_dai) - min(do_dai) > lech:
            if len(hien) >= toi_thieu:
                ra.append(hien)
            hien = []
        hien.append((dong, n))
    if len(hien) >= toi_thieu:
        ra.append(hien)
    return ra


def nhip_cau(sach):
    cau = tach_cau(sach)
    tong = max(len(cau), 1)
    chuoi = chuoi_deu(cau)
    ngan = sum(1 for _, n in cau if n < 10) * 100 / tong
    dai = sum(1 for _, n in cau if n > 25) * 100 / tong
    return {
        "so_cau": len(cau), "ngan": round(ngan), "vua": round(100 - ngan - dai) if cau else 0,
        "dai": round(dai), "chuoi_deu": len(chuoi), "dong_chuoi": [c[0][0] for c in chuoi],
        "can_xem": len(cau) >= 8 and (len(chuoi) >= 2 or ngan < 10),
    }


def phan_tich(van_ban):
    sach = bo_code(van_ban)
    thap = sach.lower()
    so_chu = max(len(TU.findall(sach)), 1)
    ket_qua = quet_nhom(thap, so_chu) + quet_dac_biet(sach, thap, so_chu)
    nhip = nhip_cau(sach)
    if nhip["can_xem"]:
        ket_qua.append(("V6", "Nhịp câu đều, khó theo dõi", 1, nhip["dong_chuoi"] or [1]))
    tong = sum(k[2] for k in ket_qua)
    return {"so_chu": so_chu, "tong": tong, "mat_do": round(tong * 1000 / so_chu, 1),
            "ket_qua": ket_qua, "nhip": nhip}


def in_van_ban(kq, nguong):
    vuot = kq["mat_do"] > nguong
    print(f"Số chữ: {kq['so_chu']}. Mẫu bắt được: {kq['tong']} lần, "
          f"{kq['mat_do']} trên 1000 chữ (ngưỡng {nguong:g}). "
          + ("VƯỢT NGƯỠNG." if vuot else "Dưới ngưỡng."))
    for ma, ten, n, vt in sorted(kq["ket_qua"], key=lambda k: -k[2]):
        dong = ", ".join(map(str, vt[:12])) + (" ..." if len(vt) > 12 else "")
        print(f"  [mẫu {ma:>3}] {ten}: {n} lần, dòng {dong}")
    if not kq["ket_qua"]:
        print("  Không thấy mẫu nào trong danh mục.")
    n = kq["nhip"]
    print(f"Nhịp câu: {n['so_cau']} câu; ngắn (dưới 10 chữ) {n['ngan']}%, vừa {n['vua']}%, "
          f"dài (trên 25 chữ) {n['dai']}%; {n['chuoi_deu']} chuỗi từ 3 câu dài gần bằng nhau.")
    if n["can_xem"]:
        print("  Câu dài đều nhau liên tiếp làm người đọc mau mệt; xen vài câu ngắn có thông tin.")
    print(GHI_CHU)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file", help='file cần soát, hoặc "-" để đọc stdin')
    ap.add_argument("--json", action="store_true", help="in kết quả dạng JSON")
    ap.add_argument("--nguong", type=float, default=NGUONG_MAC_DINH,
                    help="ngưỡng mật độ trên 1000 chữ (mặc định 15)")
    args = ap.parse_args(argv)
    if args.file == "-":
        van_ban = sys.stdin.read()
    else:
        with open(args.file, encoding="utf-8") as f:
            van_ban = f.read()
    kq = phan_tich(van_ban)
    vuot = kq["mat_do"] > args.nguong
    if args.json:
        ra = dict(kq, nguong=args.nguong, vuot_nguong=vuot, ghi_chu=GHI_CHU,
                  ket_qua=[{"ma": m, "ten": t, "so_lan": n, "dong": d}
                           for m, t, n, d in kq["ket_qua"]])
        print(json.dumps(ra, ensure_ascii=False, indent=2))
    else:
        in_van_ban(kq, args.nguong)
    return 1 if vuot else 0


if __name__ == "__main__":
    for luong in (sys.stdout, sys.stdin):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8")
    sys.exit(main())
