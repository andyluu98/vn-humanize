# -*- coding: utf-8 -*-
"""Đối chiếu số liệu và tên riêng giữa bản gốc và bản viết lại.

Cách dùng:
    python kiem-tra-so-lieu.py <goc> <moi>

Lấy từ cả hai bản: con số (1.000, 1,5, 30%, 15/11/2025, 3/2025), tên riêng nhiều
âm tiết viết hoa không đứng đầu câu (Đà Nẵng, Minh Phát) và chữ viết tắt Latin (KPI, AI).

THÊM (lỗi): có trong bản mới mà bản gốc không có. Bản viết lại không được tự thêm
số liệu hay tên.
MẤT (cảnh báo): có trong bản gốc mà bản mới không còn. MẤT có thể là chủ ý, ví dụ
người viết cố tình bỏ một chi tiết thừa, nên chỉ cảnh báo để rà lại.

Mã thoát: 1 nếu có THÊM, 0 nếu không.
"""
import re
import sys

SO = re.compile(r"(?<![\w/.,])(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}/\d{4}|\d{1,2}/\d{1,2}(?!\d)"
                r"|\d+(?:[.,]\d+)*(?:\s?%|\s+phần trăm)?)")
VIET_TAT = re.compile(r"(?<!\w)[A-Z][A-Z0-9]+(?!\w)")
CHU = re.compile(r"[^\W\d_]+")
DAU_CAU_TRUOC = re.compile(r"(?:^|[.!?:" + chr(0x2026) + r"])\W*$")


def chuan_hoa_so(so):
    so = re.sub(r"\s*phần trăm$", "%", so).replace(" ", "")
    phan = so.rstrip("%")
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", phan):
        so = phan.replace(".", "") + so[len(phan):]
    return so


def lay_so(van_ban):
    """{số đã chuẩn hóa: số dòng đầu tiên}"""
    ra = {}
    for m in SO.finditer(van_ban):
        ra.setdefault(chuan_hoa_so(m.group()), van_ban.count("\n", 0, m.start()) + 1)
    return ra


def thanh_phan(cac_so):
    """Số và các phần của ngày tháng: 15/11/2025 cho thêm 15, 11, 2025."""
    ra = set(cac_so)
    for so in cac_so:
        if "/" in so:
            ra.update(so.split("/"))
    return ra


def dau_cau(van_ban, vi_tri):
    dau_dong = van_ban.rfind("\n", 0, vi_tri) + 1
    return bool(DAU_CAU_TRUOC.search(van_ban[dau_dong:vi_tri]))


def lay_ten(van_ban):
    """{tên riêng hoặc chữ viết tắt: số dòng đầu tiên}"""
    # Bỏ dòng tiêu đề markdown: tiêu đề hay viết hoa mọi chữ, dễ nhận nhầm là tên.
    van_ban = re.sub(r"(?m)^[ \t]*#.*$", "", van_ban)
    ra, chuoi = {}, []

    def chot():
        if chuoi and dau_cau(van_ban, chuoi[0].start()):
            chuoi.pop(0)
        if len(chuoi) >= 2:
            ten = van_ban[chuoi[0].start():chuoi[-1].end()]
            ra.setdefault(ten, van_ban.count("\n", 0, chuoi[0].start()) + 1)
        chuoi.clear()

    for m in CHU.finditer(van_ban):
        tu = m.group()
        hoa = tu[0].isupper() and not (tu.isupper() and len(tu) > 1)
        lien = chuoi and van_ban[chuoi[-1].end():m.start()] == " "
        if not (hoa and (lien or not chuoi)):
            chot()
        if hoa:
            chuoi.append(m)
    chot()
    for m in VIET_TAT.finditer(van_ban):
        ra.setdefault(m.group(), van_ban.count("\n", 0, m.start()) + 1)
    return ra


def co_trong(ten, van_ban):
    return re.search(r"(?<!\w)" + re.escape(ten) + r"(?!\w)", van_ban) is not None


def doi_chieu(goc, moi):
    """Trả về (thêm, mất): mỗi phần là [(loại, giá trị, dòng)]."""
    so_goc, so_moi = lay_so(goc), lay_so(moi)
    du_goc, du_moi = thanh_phan(so_goc), thanh_phan(so_moi)
    them = [("số", s, d) for s, d in so_moi.items() if s not in du_goc]
    mat = [("số", s, d) for s, d in so_goc.items() if s not in du_moi]
    them += [("tên", t, d) for t, d in lay_ten(moi).items() if not co_trong(t, goc)]
    mat += [("tên", t, d) for t, d in lay_ten(goc).items() if not co_trong(t, moi)]
    return them, mat


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2 or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    goc, moi = (open(p, encoding="utf-8").read() for p in argv)
    them, mat = doi_chieu(goc, moi)
    if them:
        print("THÊM (lỗi): bản mới có, bản gốc không có")
        for loai, gt, d in them:
            print(f"  {loai} {gt} (bản mới, dòng {d})")
    if mat:
        print("MẤT (cảnh báo, có thể là chủ ý): bản gốc có, bản mới không còn")
        for loai, gt, d in mat:
            print(f"  {loai} {gt} (bản gốc, dòng {d})")
    if not them and not mat:
        print("Số liệu và tên riêng khớp giữa hai bản.")
    elif not them:
        print("Không có số hay tên nào được thêm.")
    return 1 if them else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
