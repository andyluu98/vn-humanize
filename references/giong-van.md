# Hồ sơ giọng văn

Hồ sơ giọng văn là bản mô tả ngắn cách một người viết thật sự viết: câu dài hay ngắn, hay dùng dấu gì, nối ý bằng từ nào, xưng hô ra sao. Có hồ sơ rồi thì mỗi lần sửa hay viết mới, bài ra gần giọng người đó hơn, thay vì về giọng trung bình của máy.

Giống như thợ may giữ số đo của khách: lần đầu đo kỹ, những lần sau may theo số đo, khách thấy vừa thì sửa số đo chứ không đo lại từ đầu.

## Cần gì để lập hồ sơ

- **Ít nhất 150 chữ** văn mẫu (chữ ở đây là âm tiết, đếm theo khoảng trắng). Càng nhiều càng tốt; 400-800 chữ là đủ dùng.
- **Do chính người viết viết**, không phải bài AI viết hộ hay bài đã qua AI sửa. Học từ bài AI thì hồ sơ sẽ học lại giọng AI.
- **Cùng loại với bài sắp viết** nếu có thể: email cũ cho email, bài đăng cũ cho bài đăng. Văn mẫu khác loại vẫn dùng được cho phần cấu trúc (độ dài câu, cách mở câu), nhưng bỏ phần thân mật khi viết bài trang trọng.

Dưới 150 chữ: vẫn đọc và theo, nhưng ghi "hồ sơ tạm", không tính tỷ lệ câu vì mẫu quá ít.

## Đọc văn mẫu, ghi những gì

| Mục | Cách lấy | Ví dụ ghi |
|---|---|---|
| Tỷ lệ độ dài câu | Tách câu theo dấu chấm, chấm hỏi, chấm than. Đếm chữ mỗi câu. Chia ba nhóm: ngắn (dưới 10 chữ), vừa (10-25), dài (trên 25) | Ngắn 30%, vừa 55%, dài 15% |
| Dấu câu hay dùng | Đếm dấu ít phổ biến: hai chấm, chấm phẩy, ngoặc đơn, ba chấm, gạch dài, chấm than | Hay dùng ngoặc đơn để chen ý; gần như không dùng chấm phẩy; không có gạch dài |
| Từ nối ưa dùng | Ghi những từ nối lặp lại nhiều lần | "nên", "mà", "thật ra", "kiểu như" |
| Xưng hô | Người viết gọi mình và người đọc thế nào | Xưng "mình", gọi người đọc "mọi người" |
| Mức trang trọng | Thấp, vừa, cao; kèm dấu hiệu | Vừa: ít Hán Việt, có thuật ngữ tiếng Anh giữ nguyên (deadline, KPI) |
| Thói quen riêng | Những gì khiến bài nhận ra là của người này | Mở bài bằng một câu hỏi thật với bạn đọc; hay kể số liệu đo được; hay tự sửa giữa câu ("à không, phải là...") |
| Không bao giờ dùng | Từ, cấu trúc người viết nói họ không dùng | "đồng hành", "nâng tầm"; câu bắt đầu bằng "Việc" |
| Câu mẫu nhịp | Chép nguyên văn 3-5 câu tiêu biểu, cả câu ngắn và câu dài | (xem mẫu bên dưới) |

Đếm bằng tay được, hoặc nhờ một đoạn Python ngắn tách câu và đếm khoảng trắng. Con số chỉ để định hướng; đừng ép bài mới khớp từng phần trăm.

## Lưu hồ sơ

- Lưu thành `ho-so-giong-van.md` trong thư mục làm việc của người dùng (thư mục chứa bài đang sửa, hoặc thư mục người dùng chỉ định).
- Đã có file cùng tên: **hỏi trước khi ghi đè**. Người dùng đồng ý thì chuyển bản cũ vào `_backup/` cạnh file, tên `ho-so-giong-van_yymmdd-HHmm.md`, rồi mới ghi bản mới.
- Một người viết nhiều loại văn rất khác nhau thì giữ một file, chia mục theo loại (ví dụ "Email công việc", "Bài đăng Facebook").

## Cập nhật hồ sơ

- Người dùng nói "mình không bao giờ nói thế", "không phải giọng mình", "mình hay viết là..." thì ghi ngay vào hồ sơ: chữ bị chê vào mục "Không bao giờ dùng", cách nói đúng vào "Thói quen riêng". Báo một dòng là đã cập nhật.
- Người dùng đưa thêm văn mẫu thì tính lại tỷ lệ câu trên toàn bộ mẫu, không chỉ phần mới.
- Ghi ngày cập nhật cuối ở đầu file.

## Dùng hồ sơ khi sửa, khi viết

- Hồ sơ thắng bảng giọng theo thể loại trong `SKILL.md`, kể cả quy tắc gạch dài: người viết hay dùng gạch dài thì giữ đúng tỷ lệ của họ.
- Hồ sơ vênh với thể loại (giọng Facebook mà đang viết tiểu luận): giữ thói quen cấu trúc (độ dài câu, cách mở câu, từ nối, cách lập luận), bỏ dấu hiệu thân mật (trợ từ, emoji, tiếng lóng).
- Hồ sơ không cho phép thêm thông tin. Biết người viết hay kể số liệu không có nghĩa là được bịa số liệu; thiếu thì hỏi theo `khai-thac-chi-tiet.md`.

## Mẫu điền

```markdown
# Hồ sơ giọng văn: [tên người viết]

Cập nhật lần cuối: dd/mm/yyyy
Nguồn văn mẫu: [bài nào, khoảng bao nhiêu chữ]
Trạng thái: [đủ mẫu | hồ sơ tạm]

## Nhịp câu
- Ngắn (dưới 10 chữ): ...%
- Vừa (10-25 chữ): ...%
- Dài (trên 25 chữ): ...%
- Ghi chú: [ví dụ: hay kết đoạn bằng một câu ngắn có thông tin]

## Dấu câu
- Hay dùng: ...
- Ít hoặc không dùng: ...

## Từ nối ưa dùng
- ...

## Xưng hô
- Tự xưng: ...
- Gọi người đọc: ...

## Mức trang trọng
- [thấp | vừa | cao]: [dấu hiệu]

## Thói quen riêng
- ...

## Không bao giờ dùng
- ...

## Câu mẫu nhịp (nguyên văn)
1. "..."
2. "..."
3. "..."

## Theo loại văn (nếu khác nhau)
### [Loại 1]
- ...
```
