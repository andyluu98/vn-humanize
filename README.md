# VN Humanize

Skill cho Claude Code (và các agent hỗ trợ skill) giúp viết lại văn bản tiếng Việt có giọng AI cho tự nhiên, giống người viết thật, mà **giữ nguyên nội dung**.

Phát triển từ [blader/humanizer](https://github.com/blader/humanizer) (MIT), dịch và viết lại toàn bộ ví dụ cho tiếng Việt, thêm 6 mẫu riêng của tiếng Việt (văn dịch, "việc/sự/một cách", Hán Việt quá mức, xưng hô, chêm tiếng Anh, câu dài đều nhau) và một script quét nhanh.

**Trước:**
> Chắc chắn rồi! Trong thời đại 4.0 ngày nay, AI không chỉ là một công cụ mà còn là người bạn đồng hành, đóng vai trò then chốt trong hành trình chuyển đổi số. Bên cạnh đó, việc áp dụng AI một cách hiệu quả giúp việc quản lý trở nên dễ dàng hơn, qua đó góp phần nâng tầm doanh nghiệp. Hy vọng bài viết hữu ích!

**Sau:**
> Phòng tôi bắt đầu dùng AI từ tháng trước, chủ yếu để soạn email và tóm tắt biên bản họp. Việc quản lý dễ hơn vì báo cáo tuần giờ có trong 15 phút thay vì cả buổi chiều.

(Bản "Sau" dùng chi tiết người viết cung cấp. Skill không tự bịa chi tiết; thiếu thì hỏi lại.)

## Skill này làm gì và không làm gì

- **Làm:** bỏ các dấu vết AI (33 mẫu), giữ giọng người viết theo văn mẫu, giữ nguyên số liệu, tên, trích dẫn.
- **Không làm:** không cài lỗi chính tả, ký tự ẩn hay mẹo để lách máy dò AI. Văn đã sửa vẫn có thể bị công cụ phát hiện AI gắn cờ; chính repo gốc cũng ghi qua mặt máy dò không phải mục tiêu.
- **Với bài nộp có chấm điểm, bài báo, luận văn:** nhiều nơi yêu cầu khai báo việc dùng AI (ví dụ COPE, ICMJE). Skill sẽ nhắc một dòng khi gặp loại văn bản này.

## Cài đặt

### Claude Code (toàn máy)

Windows (PowerShell):
```powershell
git clone https://github.com/andyluu98/vn-humanize "$HOME\.claude\skills\vn-humanize"
```

macOS, Linux:
```bash
git clone https://github.com/andyluu98/vn-humanize ~/.claude/skills/vn-humanize
```

Cập nhật bản mới: chạy `git pull` trong thư mục trên.

### Chỉ cho một dự án

Clone vào `.claude/skills/vn-humanize` bên trong thư mục dự án.

## Cách dùng

```text
/vn-humanize

[Dán đoạn văn cần sửa]
```

Theo giọng của chính mình (nên dùng):
```text
/vn-humanize

Đây là một đoạn mình tự viết trước đây để làm mẫu giọng văn:
[dán 1 tới 2 đoạn văn thật]

Sửa đoạn dưới đây theo đúng giọng đó:
[dán đoạn cần sửa]
```

Muốn học cách tự sửa: thêm câu "giải thích từng chỗ sửa theo số mẫu".

Sửa thẳng trong file: "dùng vn-humanize sửa file bai-tap.md". Bản cũ được sao lưu vào `_backup/` cạnh file.

### Quét nhanh không cần AI

```bash
python scripts/quet-dau-vet.py bai-viet.txt
```

Script liệt kê từ sáo, gạch dài, emoji, lời chatbot, mở bài khuôn kèm số dòng. Script chỉ bắt dấu vết về chữ; dấu vết về cấu trúc (bộ ba, câu chốt, văn dịch) vẫn cần đọc.

## Cấu trúc

| File | Nội dung |
|---|---|
| `SKILL.md` | Nguyên tắc, quy trình, giọng văn, cách trả lời |
| `references/cac-mau-dau-vet-ai.md` | 33 mẫu dấu vết, mỗi mẫu có ví dụ trước và sau |
| `references/nguyen-tac-bo-sung.md` | Nguyên tắc riêng thêm dần từ bài thật của học viên; ưu tiên hơn mẫu chung |
| `scripts/quet-dau-vet.py` | Quét nhanh dấu vết dạng chữ |
| `CHANGELOG.md` | Lịch sử thay đổi |

## Đóng góp

Thấy một kiểu văn AI tiếng Việt chưa có trong danh mục: mở issue kèm một câu "Trước" và câu "Sau".

## Giấy phép

MIT. Giữ nguyên ghi công cho blader/humanizer (Siqi Chen) theo giấy phép gốc.
