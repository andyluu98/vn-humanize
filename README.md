# VN Humanize

Skill cho Claude Code (và các agent hỗ trợ skill) giúp văn tiếng Việt viết có AI hỗ trợ đọc lên như chính người viết: nhịp tự nhiên, đúng giọng, có chi tiết thật, **giữ nguyên nội dung**.

Phát triển từ [blader/humanizer](https://github.com/blader/humanizer), tham khảo thêm 4 repo khác (xem mục Nguồn). Toàn bộ ví dụ viết riêng cho tiếng Việt, có 51 mẫu dấu vết AI, hồ sơ giọng văn, bảng tự kiểm, script quét và script đối chiếu số liệu.

**Trước:**
> Chắc chắn rồi! Trong thời đại 4.0 ngày nay, AI không chỉ là một công cụ mà còn là người bạn đồng hành, đóng vai trò then chốt trong hành trình chuyển đổi số. Bên cạnh đó, việc áp dụng AI một cách hiệu quả giúp việc quản lý trở nên dễ dàng hơn, qua đó góp phần nâng tầm doanh nghiệp. Hy vọng bài viết hữu ích!

**Sau:**
> Phòng tôi bắt đầu dùng AI từ tháng trước, chủ yếu để soạn email và tóm tắt biên bản họp. Việc quản lý dễ hơn vì báo cáo tuần giờ có trong 15 phút thay vì cả buổi chiều.

(Bản "Sau" dùng chi tiết người viết cung cấp khi được hỏi. Skill không tự bịa chi tiết.)

## Cách hạ "giọng AI" mà skill dùng

Văn bị coi là "giống AI" vì nó chung chung, đều đều và đầy khuôn. Skill xử lý đúng ba thứ đó:

1. **Bỏ khuôn:** 51 mẫu dấu vết, từ "không chỉ... mà còn", "đóng vai trò then chốt" tới văn dịch và "việc, sự, một cách" dày đặc.
2. **Thêm điều chỉ người viết có:** skill hỏi học viên ví dụ từ công việc của mình, con số tự đo, chuyện xảy ra khi nào, ở đâu (`references/khai-thac-chi-tiet.md`). Đây là cách hiệu quả nhất, vì AI không tự có những chi tiết này.
3. **Viết theo giọng của chính người viết:** đưa 150 chữ văn tự viết trở lên, skill lập hồ sơ giọng (độ dài câu, cách xưng hô, từ nối hay dùng) rồi sửa theo đó.

Skill **không** dùng mẹo lừa máy dò: không cài lỗi chính tả, không ký tự ẩn, không ký tự giả chữ Việt, không dịch vòng, không thay từ đồng nghĩa hàng loạt. Các mẹo này làm bài tệ đi và dễ bị phát hiện. Không công cụ nào đảm bảo bài qua được máy dò AI; skill cũng không hứa điều đó.

Bài nộp có chấm điểm, bài báo, luận văn: nhiều nơi yêu cầu khai báo việc dùng AI (ví dụ COPE, ICMJE). Skill nhắc một dòng khi gặp loại văn bản này.

## Cài đặt

Windows (PowerShell):
```powershell
git clone https://github.com/andyluu98/vn-humanize "$HOME\.claude\skills\vn-humanize"
```

macOS, Linux:
```bash
git clone https://github.com/andyluu98/vn-humanize ~/.claude/skills/vn-humanize
```

Cập nhật: chạy `git pull` trong thư mục trên. Chỉ dùng cho một dự án: clone vào `.claude/skills/vn-humanize` trong thư mục dự án.

## Cách dùng

**Sửa bài (mặc định):**
```text
/vn-humanize
[dán bài cần sửa]
```

**Sửa theo giọng của mình (nên dùng):**
```text
/vn-humanize
Đây là đoạn mình tự viết trước đây, làm mẫu giọng văn:
[dán 150 chữ trở lên văn tự viết]

Sửa bài dưới đây theo đúng giọng đó:
[dán bài cần sửa]
```

**Chỉ soát, tự sửa:** "/vn-humanize soát bài này". Skill trả bảng gồm câu trích, số mẫu và gợi ý; không chấm điểm, không đoán ai viết.

**Viết mới:** "/vn-humanize viết bài đăng Facebook về buổi học hôm nay". Skill hỏi chi tiết thật trước rồi mới viết.

**Học cách tự sửa:** thêm "giải thích từng chỗ sửa theo số mẫu".

## Script dùng không cần AI

```bash
python scripts/quet-dau-vet.py bai-viet.txt            # quét dấu vết, báo số dòng
python scripts/quet-dau-vet.py bai-viet.txt --json     # kết quả dạng JSON
python scripts/kiem-tra-so-lieu.py ban-goc.txt ban-sua.txt   # số, tên bị thêm hoặc mất
```

- Script quét đếm các mẫu có tên trên 1000 chữ (ngưỡng mặc định 15, đổi bằng `--nguong`) và báo nhịp câu. Script chỉ đếm dấu vết, **không phải máy dò AI**, không đưa ra xác suất ai viết. Kiểm tra trên 3 bài Wikipedia tiếng Việt do người viết: 0,8 tới 3,7 lần trên 1000 chữ, dưới ngưỡng.
- Script đối chiếu báo THÊM (số, tên có trong bản sửa mà bản gốc không có: lỗi) và MẤT (cảnh báo, có thể là chủ ý).

## Cấu trúc

| File | Nội dung |
|---|---|
| `SKILL.md` | 9 nguyên tắc, 3 chế độ, quy trình, giọng theo thể loại, nhịp câu |
| `references/cac-mau-dau-vet-ai.md` | 51 mẫu dấu vết có ví dụ trước và sau; dấu hiệu người viết thật cần giữ; những điều không phải dấu hiệu AI |
| `references/giong-van.md` | Cách lập hồ sơ giọng văn từ văn mẫu |
| `references/bang-tu-kiem.md` | Bảng tự kiểm đạt hoặc không đạt, lặp tới khi qua hết |
| `references/khai-thac-chi-tiet.md` | Câu hỏi lấy chi tiết thật từ người viết, theo thể loại |
| `references/nguyen-tac-bo-sung.md` | Nguyên tắc riêng thêm dần từ bài thật của học viên; ưu tiên hơn mẫu chung |
| `scripts/quet-dau-vet.py` | Quét dấu vết dạng chữ và nhịp câu |
| `scripts/kiem-tra-so-lieu.py` | Đối chiếu số, tên giữa bản gốc và bản sửa |
| `tests/` | Cặp bài trước và sau theo 5 thể loại, văn người viết không được báo nhầm |

Chạy test: `python -m pytest -q`.

## Đóng góp

Thấy một kiểu văn AI tiếng Việt chưa có trong danh mục: mở issue kèm một câu "Trước" và một câu "Sau".

## Nguồn

- [blader/humanizer](https://github.com/blader/humanizer) (MIT): khung danh mục và quy trình.
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) qua [ryanmaule/humanize](https://github.com/ryanmaule/humanize) (MIT): sửa tối thiểu, chế độ soát, bảng tự kiểm.
- [shir-danishyar/humanize](https://github.com/shir-danishyar/humanize) (MIT): hồ sơ giọng văn, quy tắc theo thể loại, ngân sách trong script quét, test chống bịa số.
- [korECM/humanize](https://github.com/korECM/humanize): ý tưởng về câu gói ý, cân bằng hai phía, từ thừa nghĩa.
- [David-Saeteros/claude-skills](https://github.com/David-Saeteros/claude-skills) (CC BY 4.0): ý tưởng về độ mạnh khẳng định, định lượng mơ hồ, tổng quan liệt kê.
- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

Phần chữ và ví dụ trong repo này viết lại bằng tiếng Việt, không chép nguyên văn các nguồn trên.

## Giấy phép

MIT. Xem `LICENSE`.
