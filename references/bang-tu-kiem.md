# Bảng tự kiểm

Chạy bảng này trên bản nháp trước khi viết bản cuối (bước 8 của quy trình). Mỗi mục chỉ có hai kết quả: Qua hoặc Trượt.

**Quy tắc:** trượt một mục thì sửa chỗ đó, rồi chạy lại **toàn bộ** bảng từ đầu, vì sửa chỗ này hay làm hỏng chỗ khác (bỏ một bộ ba có thể làm ba câu liền nhau dài bằng nhau). Lặp tới khi qua hết.

## 1. Nội dung

- [ ] Không thêm, không mất số liệu, tên người, tên tổ chức, ngày tháng, trích dẫn, nguồn. Chạy `python scripts/kiem-tra-so-lieu.py <goc> <moi>` để đối chiếu, rồi đọc lại những chỗ script báo.
- [ ] Mỗi ý của bản gốc còn trong bản nháp, hoặc bị bỏ vì một mẫu cụ thể yêu cầu bỏ (ghi được số mẫu).
- [ ] Không có câu nào khẳng định mạnh hơn nguồn: "có thể" không thành "chắc chắn", "nhóm khảo sát" không thành "mọi người", "tăng" không thành "tăng mạnh".
- [ ] Không có chi tiết nào bịa thêm. Chi tiết mới đều do người viết cung cấp trong cuộc trò chuyện.
- [ ] Không có mẹo lừa máy dò: không lỗi chính tả cố ý, không ký tự ẩn, không ký tự trông giống chữ Việt, không dấu câu thất thường cố ý.

## 2. Dấu vết

Quét lại những mẫu hay sống sót sau lần sửa đầu:

- [ ] Mẫu 1: không còn "không chỉ... mà còn", "không phải A mà là B" thừa.
- [ ] Mẫu 2: không còn câu chốt một dòng nhắc lại ý vừa nói.
- [ ] Mẫu 7: không còn bộ ba gượng ép.
- [ ] Mẫu 9: không còn đoạn nào cũng mở bằng từ nối.
- [ ] Mẫu 10: không còn gạch dài (U+2014) hay gạch vừa (U+2013), trừ khi văn mẫu của người viết có dùng.
- [ ] Mẫu 13: không còn từ sáo đi thành cụm. Chạy lại `python scripts/quet-dau-vet.py <file>`.
- [ ] Mẫu 28: không còn hai chấm lật bài ("Kết quả: ...", "Lý do rất đơn giản: ...").
- [ ] Mẫu 29: không còn tự hỏi tự trả lời ("Vậy tại sao? Vì...").
- [ ] Mẫu V2: không còn "việc", "sự", "một cách" đầy câu.

## 3. Nhịp

- [ ] Không có ba câu liền nhau dài xấp xỉ bằng nhau.
- [ ] Không có hai, ba câu dài liền nhau cùng cấu trúc.
- [ ] Mỗi đoạn có ít nhất một câu ngắn có thông tin.
- [ ] Đọc to ba câu bất kỳ liền nhau: không phải lấy hơi giữa câu, không nghe như đọc danh sách.

## 4. Giọng

- [ ] Người viết đọc có nhận ra bài là của mình không? So với hồ sơ giọng văn hoặc văn mẫu nếu có: xưng hô, từ nối, độ dài câu, thói quen riêng.
- [ ] Đọc to cho một đồng nghiệp tinh ý nghe, bài có tự nhiên không? Chỗ nào người đó sẽ nhíu mày thì sửa chỗ đó.
- [ ] Sau khi đọc, liệt kê lại được điều người đọc học được hoặc cần làm không? Không liệt kê được thì bài còn trống rỗng; quay lại `khai-thac-chi-tiet.md`.
- [ ] Xưng hô nhất quán từ đầu tới cuối, đúng thể loại (bảng thể loại trong `SKILL.md`).
- [ ] Mức trang trọng không cao hơn bản gốc.

## 5. Mức sửa

- [ ] Tỷ lệ sửa tương xứng với bài. Văn do người viết tự viết: sửa quá khoảng 30% số câu thì rà lại từng chỗ, chỗ nào không chỉ được dấu vết hay lỗi cụ thể thì trả về câu gốc. Bài AI viết gần như toàn bộ: được viết lại nhiều hơn.
- [ ] Câu người viết viết tốt vẫn còn nguyên.
- [ ] Ngôi kể giữ như bản gốc: văn tổ chức ngôi thứ ba không bị đổi thành "tôi".
