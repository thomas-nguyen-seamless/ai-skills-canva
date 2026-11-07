# Brief template for `create-design` (Vietnamese class deck, talk mode)

Paste into the `brief` argument after filling every <...>. Keep it < ~2,500 characters. The outline carries the per-slide content; the brief carries the stance.

```
Bài thuyết trình đúng <N> slide, định dạng slide 16:9 nhiều trang, không phải poster, flyer hay tài liệu một trang.

Chủ đề: <môn / chủ đề>. Khán giả: <giảng viên và sinh viên>. Mục tiêu: <giải thích khái niệm, nội dung, ví dụ, ý nghĩa>. Ngôn ngữ: tiếng Việt có dấu đầy đủ, văn phong học thuật, thuật ngữ nhất quán và chính xác theo giáo trình.

Chế độ talk: tối đa 4 gạch đầu dòng và khoảng 40 từ mỗi slide, mỗi ý ngắn. Mạch trình bày: <câu mạch một câu>. Kết bằng slide takeaway.

Phong cách thiết kế: nền <sáng/tối: mã màu>, MỘT màu nhấn <mã màu>, chữ sans-serif hỗ trợ tiếng Việt, hình ảnh <phẳng, vector, tối giản / tranh khắc theo ảnh người dùng>, mật độ cân bằng, lề rộng, mọi slide dùng cùng một lưới, tiêu đề cùng vị trí.

Tránh: 3D, gradient, đổ bóng, clip-art, ảnh stock, emoji, gạch hoặc vạch màu dưới tiêu đề, viền một cạnh, căn giữa toàn bộ, chữ in hoa (trừ tiêu đề bìa), số thứ tự 01/02/03 khi các mục không theo trình tự.

Chữ lớn dễ đọc ở cuối lớp: tiêu đề ngắn, nội dung ngắn gọn, nhiều khoảng trắng có chủ đích. Slide sơ đồ chỉ có tiêu đề và một vùng trống lớn bên dưới, không vẽ minh hoạ. Slide ví dụ vẽ chuỗi ba khối bằng nhau nối bằng mũi tên, chú thích ngắn dưới mỗi khối.

Thuật ngữ bắt buộc đúng: <danh sách thuật ngữ, ví dụ: khách quan, kế thừa, phổ biến>.
```

Calls: `create-design { brief, format:"Presentation (16:9)", outline:{sections:[...]}, user_intent }`; then poll `get-create-design-async-job { job_id, continuation_token }` every >= 15 s until `completed`.
