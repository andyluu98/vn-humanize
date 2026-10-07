# -*- coding: utf-8 -*-
"""Kiểm thử quet-dau-vet.py và kiem-tra-so-lieu.py trên bộ mẫu trong tests/mau/."""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

GOC = Path(__file__).resolve().parent.parent
MAU = GOC / "tests" / "mau"
QUET = GOC / "scripts" / "quet-dau-vet.py"
SO_LIEU = GOC / "scripts" / "kiem-tra-so-lieu.py"
GACH_DAI = chr(0x2014)  # không viết thẳng ký tự vào file


def nap(duong_dan, ten):
    spec = importlib.util.spec_from_file_location(ten, duong_dan)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


quet = nap(QUET, "quet_dau_vet")
so_lieu = nap(SO_LIEU, "kiem_tra_so_lieu")

TRUOC = sorted(MAU.glob("*-truoc.txt"))
SAU = sorted(MAU.glob("*-sau.txt"))
NGUOI_VIET = sorted(MAU.glob("nguoi-viet-*.txt"))


def chay(script, *args, stdin=None):
    return subprocess.run([sys.executable, str(script), *map(str, args)], input=stdin,
                          capture_output=True, encoding="utf-8")


def ma(van_ban):
    return {k[0] for k in quet.phan_tich(van_ban)["ket_qua"]}


def doc(p):
    return p.read_text(encoding="utf-8")


def test_du_bo_mau():
    assert len(TRUOC) >= 5 and len(SAU) == len(TRUOC) and len(NGUOI_VIET) >= 3


@pytest.mark.parametrize("p", TRUOC, ids=lambda p: p.name)
def test_ban_truoc_vuot_nguong(p):
    r = chay(QUET, p)
    assert r.returncode == 1, r.stdout


@pytest.mark.parametrize("p", SAU + NGUOI_VIET, ids=lambda p: p.name)
def test_ban_tu_nhien_duoi_nguong(p):
    r = chay(QUET, p)
    assert r.returncode == 0, r.stdout


@pytest.mark.parametrize("p", NGUOI_VIET, ids=lambda p: p.name)
def test_van_nguoi_viet_khong_bi_bat(p):
    assert quet.phan_tich(doc(p))["ket_qua"] == []


@pytest.mark.parametrize("p", NGUOI_VIET, ids=lambda p: p.name)
def test_van_nguoi_viet_du_dai(p):
    assert 120 <= quet.phan_tich(doc(p))["so_chu"] <= 250


def test_json_va_ghi_chu():
    r = chay(QUET, "-", "--json", stdin=doc(TRUOC[0]))
    kq = json.loads(r.stdout)
    assert kq["vuot_nguong"] and r.returncode == 1
    assert kq["mat_do"] > kq["nguong"] == 15
    assert "không đoán" in kq["ghi_chu"]
    assert "không đoán" in chay(QUET, SAU[0]).stdout


def test_nguong_tuy_chinh():
    assert chay(QUET, TRUOC[0], "--nguong", "1000").returncode == 0


def test_hai_cham_lat_bai():
    assert "28" in ma("Điểm hay nhất: khách tự đặt lịch mà không cần gọi điện.")
    assert "28" in ma("Mình thử cả tuần. Kết quả: không còn đau lưng nữa.")
    assert "28" not in ma("Thời gian: 9 giờ sáng thứ Hai.")


def test_tu_hoi_tu_tra_loi():
    assert "29" in ma("Vì sao? Vì khách hàng cần câu trả lời ngay trong ngày.")
    assert "29" in ma("Bạn có biết mỗi ngày nên uống bao nhiêu nước không?")
    assert "29" not in ma("Ai đi Đà Lạt tuần này không? Mình còn dư một vé xe.")


def test_gach_dai_theo_ngan_sach():
    cau = "Nhóm họp lúc chín giờ sáng để chốt kế hoạch tuần sau cho cả phòng. "
    mot = cau * 3 + f"Kết quả {GACH_DAI} như mọi khi {GACH_DAI} chưa có gì."
    assert "10" not in ma(cau * 3 + f"Kết quả {GACH_DAI} chưa có gì.")
    assert "10" in ma(mot)
    assert "10" not in ma("Giai đoạn 2020" + chr(0x2013) + "2025 có ba đợt tuyển.")


def test_gach_trong_code_bi_bo_qua():
    van_ban = f"Chạy lệnh sau.\n```\na {GACH_DAI} b {GACH_DAI} c {GACH_DAI} d\n```\nGõ `x {GACH_DAI} y` là xong."
    assert "10" not in ma(van_ban)


def test_ngoac_kep_tron():
    cong = chr(0x201C) + "đẹp" + chr(0x201D)
    assert "22" in ma(f'Anh ấy nói {cong} rồi lại bảo "thôi".')
    assert "22" not in ma(f"Anh ấy nói {cong} rồi đi.")
    assert "22" not in ma('Anh ấy nói "đẹp" rồi đi.')


def test_tu_noi_theo_ngan_sach():
    assert "9" not in ma("Ngoài ra, phòng còn hai máy in. Tuy nhiên, một máy đang hỏng.")
    assert "9" in ma("Ngoài ra, có A. Bên cạnh đó, có B. Hơn nữa, có C.")


def test_cho_trong_mau():
    assert "39" in ma("Kính gửi [Tên khách hàng], doanh thu tăng XX% so với cùng kỳ.")
    assert "39" not in ma("Xem [hướng dẫn](https://example.com) để biết thêm.")


def test_mau_moi_khac():
    assert "30" in ma("Không phải vì tiền. Không phải vì danh tiếng.")
    assert "31" in ma("Con số biết nói: doanh thu tăng gấp đôi.")
    assert "36" in ma("AI là con dao hai lưỡi.")
    assert "38" in ma("KPI là viết tắt của Key Performance Indicator.\nNó dùng để đo kết quả.")
    assert "42" in ma("Cần nghiên cứu thêm để kết luận.")
    assert "V8" in ma("Họ quay trở lại sau ba tháng.")
    assert "35" in ma("Tức là A. Nói cách khác là B. Điều này có nghĩa là C.")


def test_nhip_cau_deu():
    dai = ("Nhóm dự án đã họp với khách hàng để thống nhất phạm vi công việc và thời hạn "
           "bàn giao của giai đoạn đầu tiên. ")
    kq = quet.phan_tich(dai * 9)
    assert kq["nhip"]["ngan"] == 0 and kq["nhip"]["chuoi_deu"] >= 1
    assert "V6" in {k[0] for k in kq["ket_qua"]}
    xen = (dai + "Khách đồng ý ngay. ") * 5
    assert "V6" not in ma(xen)


@pytest.mark.parametrize("p", TRUOC, ids=lambda p: p.name)
def test_ban_sau_khong_them_so_lieu(p):
    sau = p.with_name(p.name.replace("-truoc", "-sau"))
    them, _ = so_lieu.doi_chieu(doc(p), doc(sau))
    assert them == []
    assert chay(SO_LIEU, p, sau).returncode == 0


def test_bia_so_lieu_bi_bat(tmp_path):
    goc, moi = tmp_path / "goc.txt", tmp_path / "moi.txt"
    goc.write_text("Doanh thu quý 3 tăng 18%, đạt 4,2 tỷ đồng.", encoding="utf-8")
    moi.write_text("Doanh thu quý 3 tăng 25%, đạt 4,2 tỷ đồng ở Hải Phòng.", encoding="utf-8")
    r = chay(SO_LIEU, goc, moi)
    assert r.returncode == 1
    assert "25%" in r.stdout and "Hải Phòng" in r.stdout and "18%" in r.stdout


def test_lay_so_va_ten():
    van_ban = "Ngày 15/11/2025 công ty Minh Phát chi 1.000 triệu, tăng 1,5 lần, đạt 30 phần trăm KPI."
    assert {"15/11/2025", "1000", "1,5", "30%"} <= set(so_lieu.lay_so(van_ban))
    ten = set(so_lieu.lay_ten(van_ban))
    assert {"Minh Phát", "KPI"} <= ten and "Ngày" not in ten
