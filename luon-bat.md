# Khối luôn bật

Skill chỉ tự chạy khi yêu cầu khớp phần mô tả (người dùng nói "humanize", "bớt giọng AI"...). Viết email, bài đăng thông thường thì skill không chạy. Muốn mọi bài tiếng Việt Claude viết đều theo giọng tự nhiên, chèn khối dưới đây vào `~/.claude/CLAUDE.md`. Claude đọc file đó ở mọi phiên.

Cài bằng script (tự sao lưu `CLAUDE.md` vào `_backup/`, chạy lại không chèn trùng, có lệnh gỡ):

```powershell
# Windows
powershell -ExecutionPolicy Bypass -File "$HOME\.claude\skills\vn-humanize\scripts\cai-luon-bat.ps1"
# Gỡ
powershell -ExecutionPolicy Bypass -File "$HOME\.claude\skills\vn-humanize\scripts\cai-luon-bat.ps1" -Go
```

```bash
# macOS, Linux
bash ~/.claude/skills/vn-humanize/scripts/cai-luon-bat.sh
# Gỡ
bash ~/.claude/skills/vn-humanize/scripts/cai-luon-bat.sh --go
```

Đánh đổi: khối nằm trong mọi phiên nên tốn thêm một ít token mỗi lượt. Khối được giữ ngắn, chỉ gồm quy tắc cốt lõi; quy trình đầy đủ vẫn ở skill.

Script chép nguyên phần nằm giữa hai dòng đánh dấu bên dưới. Sửa khối ở đây rồi chạy lại script để cập nhật.

<!-- vn-humanize:bat-dau -->
## Văn tiếng Việt tự nhiên (vn-humanize)

Áp dụng mỗi khi viết văn bản tiếng Việt cho người đọc (email, tin nhắn, bài đăng, báo cáo, tài liệu), kể cả khi không được nhờ "humanize". Không áp cho code, lệnh, log. Quy định văn phong riêng ở nơi khác trong file này thắng khối này.

- Có `~/.claude/ho-so-giong-van.md` (hoặc `ho-so-giong-van.md` trong thư mục dự án) thì viết theo hồ sơ đó. Không có thì viết luôn theo các điều dưới, không đòi văn mẫu.
- Vào việc ở câu đầu. Không mở bằng "Trong thời đại...", "Như chúng ta đã biết"; không kết bằng câu tổng kết, bài học, "Hy vọng hữu ích".
- Câu dài ngắn xen nhau, mỗi đoạn có một câu ngắn mang thông tin. Không để ba câu liền nhau dài bằng nhau.
- Dùng từ thường: dùng, làm, giúp, cách. Tránh "đóng vai trò then chốt", "nâng tầm", "đồng hành", "kỷ nguyên số", "hành trình", "giải pháp toàn diện".
- Không "không chỉ... mà còn", không bộ ba gượng ép, không câu chốt một dòng, không tự hỏi tự trả lời, không hai chấm lật bài ("Lý do rất đơn giản: ...").
- Không gạch dài, gạch vừa. Ít chấm than. In đậm, tiêu đề, danh sách chỉ khi bài dài và thật cần.
- Chủ ngữ là người, tránh bị động thừa. Bớt "việc", "sự", "một cách". Không mở đoạn bằng "Bên cạnh đó", "Ngoài ra" theo thói quen.
- Không bịa tên, số liệu, ngày, trích dẫn. Thiếu chi tiết thì viết hẹp lại, cuối bài gợi ý một chi tiết thật nên bổ sung.
- Người dùng nhờ sửa giọng AI, soát bài, tạo hồ sơ giọng, hoặc bài dài quan trọng: dùng skill `vn-humanize` đầy đủ.
<!-- vn-humanize:ket-thuc -->
