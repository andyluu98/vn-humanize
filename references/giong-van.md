# Hồ sơ giọng văn

Hồ sơ giọng văn là bản mô tả ngắn cách một người viết thật sự viết: câu dài hay ngắn, hay dùng dấu gì, nối ý bằng từ nào, xưng hô ra sao. Có hồ sơ rồi thì mỗi lần sửa hay viết mới, bài ra gần giọng người đó hơn, thay vì về giọng trung bình của máy.

Giống như thợ may giữ số đo của khách: lần đầu đo kỹ, những lần sau may theo số đo, khách thấy vừa thì sửa số đo chứ không đo lại từ đầu.

## Cần gì để lập hồ sơ

- **Ít nhất 150 chữ** văn mẫu (chữ ở đây là âm tiết, đếm theo khoảng trắng). Càng nhiều càng tốt; 400-800 chữ là đủ dùng.
- **Do chính người viết viết**, không phải bài AI viết hộ hay bài đã qua AI sửa. Học từ bài AI thì hồ sơ sẽ học lại giọng AI.
- **Cùng loại với bài sắp viết** nếu có thể: email cũ cho email, bài đăng cũ cho bài đăng. Văn mẫu khác loại vẫn dùng được cho phần cấu trúc (độ dài câu, cách mở câu), nhưng bỏ phần thân mật khi viết bài trang trọng.

Dưới 150 chữ: vẫn đọc và theo, nhưng ghi "hồ sơ tạm", không tính tỷ lệ câu vì mẫu quá ít.

Không có văn mẫu nào: lập hồ sơ tạm bằng trắc nghiệm (mục "Tạo hồ sơ khi chưa có văn mẫu"), hoặc cứ viết theo `giong-mac-dinh.md`. Văn mẫu là để bài giống người viết hơn, không phải điều kiện để bắt đầu.

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

## Tạo hồ sơ khi chưa có văn mẫu

Nhiều người không có sẵn 150 chữ tự viết. Khi đó không đòi văn mẫu; hỏi 6 câu trắc nghiệm, mỗi lượt tối đa 3 câu, mỗi câu có lựa chọn sẵn và cho trả lời khác:

1. Bạn thường viết gì nhất? (email công việc / bài đăng mạng xã hội / báo cáo, bài tập / tin nhắn nhóm)
2. Bạn xưng hô thế nào trong loại văn đó? (tôi / mình / em, anh chị / theo người nhận)
3. Câu của bạn thường thế nào? (ngắn gọn, đi thẳng / vừa phải / dài, giải thích kỹ)
4. Mức trang trọng? (thân mật, như nói chuyện / lịch sự vừa phải / trang trọng)
5. Bạn có hay dùng trợ từ cuối câu (nhé, nha, ạ, chứ), emoji, tiếng Anh xen vào không? (chọn những cái hay dùng)
6. Có từ hay kiểu câu nào bạn ghét, không bao giờ viết không? (ví dụ "đồng hành", "nâng tầm", "Kính gửi quý anh chị")

Từ câu trả lời, lập hồ sơ theo mẫu điền bên dưới với `Trạng thái: hồ sơ tạm (từ trắc nghiệm)`, bỏ trống tỷ lệ câu và câu mẫu nhịp. Lần sau người dùng đưa văn tự viết thì bổ sung, đổi trạng thái thành "đủ mẫu".

## Lưu hồ sơ

- **Hồ sơ dùng chung (mặc định):** lưu ở `~/.claude/ho-so-giong-van.md` (Windows: `%USERPROFILE%\.claude\ho-so-giong-van.md`). Mọi lần dùng skill, ở thư mục nào, đều đọc file này trước. Nhờ vậy người dùng chỉ lập hồ sơ một lần.
- **Hồ sơ riêng một dự án:** người dùng muốn một giọng riêng cho dự án (ví dụ viết thay một người khác) thì lưu `ho-so-giong-van.md` trong thư mục dự án. Có file trong thư mục làm việc thì file đó thắng hồ sơ dùng chung.
- Đã có file cùng tên: **hỏi trước khi ghi đè**. Người dùng đồng ý thì chuyển bản cũ vào `_backup/` cạnh file, tên `ho-so-giong-van_yymmdd-HHmm.md`, rồi mới ghi bản mới.
- Một người viết nhiều loại văn rất khác nhau thì giữ một file, chia mục theo loại (ví dụ "Email công việc", "Bài đăng Facebook").
- Hồ sơ không chứa thông tin riêng tư (số điện thoại, địa chỉ, tên khách hàng). Câu mẫu nhịp có tên riêng thì thay bằng chữ chung trước khi lưu.

## Cập nhật hồ sơ

- Sửa đúng file đang dùng (riêng dự án nếu có, không thì hồ sơ dùng chung).
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
