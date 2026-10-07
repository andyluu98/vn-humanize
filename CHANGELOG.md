# Lịch sử thay đổi

## 2.0.0 (07/10/2026)

Tham khảo thêm 4 repo: ryanmaule/humanize (từ petergyang/no-ai-slop), korECM/humanize, shir-danishyar/humanize, David-Saeteros/claude-skills. Chỉ lấy ý tưởng về chất lượng văn; không lấy mẹo lừa máy dò.

- Danh mục tăng từ 33 lên 51 mẫu: thêm mẫu 28 tới 43 (hai chấm lật bài, tự hỏi tự trả lời, liệt kê phủ định, vật vô tri làm việc của người, đổi từ đồng nghĩa liên tục, "cần/nên" cuối đoạn, phạm vi giả "từ... đến...", câu gói ý lặp, cân bằng hai phía, định lượng mơ hồ, mở bằng định nghĩa, chỗ trống mẫu, khung bài thừa, tổng quan liệt kê, hạn chế chung chung, câu chủ đề đầu mọi đoạn) và V7, V8.
- Sửa mẫu cũ: câu châm ngôn thì xóa chứ không viết lại; từ nối phải mang logic; đổi gạch dài sang hai chấm có thể sinh mẫu 28; bỏ rào đón không được làm khẳng định mạnh hơn nguồn; ngoặc kép cong chỉ là dấu vết khi trộn với ngoặc thẳng.
- Thêm phần "Dấu hiệu người viết thật (giữ lại)" và "Không phải dấu hiệu AI" để tránh sửa nhầm.
- SKILL.md viết lại: ba chế độ Sửa, Soát, Viết mới; 9 nguyên tắc (thêm sửa tối thiểu, không nâng trang trọng, không bịa giọng "tôi", không mạnh hơn nguồn); bảng giọng theo thể loại có quy tắc bật tắt; mục nhịp câu.
- File mới: `references/giong-van.md` (hồ sơ giọng văn), `references/bang-tu-kiem.md` (bảng tự kiểm có vòng lặp), `references/khai-thac-chi-tiet.md` (câu hỏi lấy chi tiết thật từ người viết).
- Script quét nâng cấp: mật độ trên 1000 chữ, ngưỡng và mã thoát, `--json`, bỏ qua code, ngân sách cho gạch dài và từ nối, thêm các mẫu mới, báo cáo nhịp câu.
- Script mới `scripts/kiem-tra-so-lieu.py`: báo số, tên bị thêm hoặc mất sau khi sửa.
- Bộ test `tests/` với cặp bài trước và sau theo thể loại, bài người viết tự nhiên không được báo nhầm; chạy tự động trên GitHub Actions.

## 1.0.0 (07/10/2026)

- Bản đầu tiên, phát triển từ blader/humanizer 3.1.0.
- 27 mẫu chung viết lại với ví dụ tiếng Việt; thêm mẫu 6 (mở bài, kết bài khuôn) và mẫu 9 (từ nối đầu đoạn).
- Thêm nhóm V gồm 6 mẫu riêng của tiếng Việt.
- Thêm bảng giọng văn theo loại văn bản (bài đăng, email, bài tập, công văn, học thuật).
- Thêm `references/nguyen-tac-bo-sung.md` để chủ repo bổ sung nguyên tắc.
- Thêm `scripts/quet-dau-vet.py` quét nhanh dấu vết dạng chữ.
