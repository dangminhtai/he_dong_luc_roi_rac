# Checklist: Triển khai Chaos Matrix Game (Pygame)

Dưới đây là các bước để hiện thực hóa ý tưởng từ `DDS.py` thành một trò chơi hoàn chỉnh.

- [x] Create `docs/requirements.md` with detailed game design
- [x] Create `docs/check_lists.md` for implementation tracking
- [x] Implement core game logic in `chaos_game.py`
- [x] Add interactive features (reset, speed control)
- [/] Add dynamic control for `MOD_VALUE` and `seed_matrix`
- [ ] Final verification and cleanup

## 1. Chuẩn bị môi trường
- [x] Cài đặt thư viện `pygame` (`pip install pygame`)
- [x] Tạo file source chính `chaos_game.py`
- [x] Tổ chức lại module `linear/det.py` để dùng chung

## 2. Xây dựng Engine DDS (Core Logic)
- [x] Chuyển đổi logic từ `DDS.py` thành một class hoặc generator để tính điểm liên tục.
- [x] Tích hợp tính năng "Modulus" để giữ giá trị trong phạm vi màn hình.
- [x] Thêm cơ chế reset ma trận hạt giống (Seed Matrix).

## 3. Khởi tạo Đồ họa (Pygame Setup)
- [x] Khởi tạo màn hình Pygame (Resolution: ví dụ 800x600 hoặc fullscreen).
- [x] Thiết lập Game Loop (Handle events, Update, Draw).
- [x] Tạo một Surface để lưu trữ các điểm đã vẽ.

## 4. Hiện thực hóa việc Vẽ (Drawing & Chaos Game)
- [x] Map giá trị `xi` thành tọa độ `(x, y)` trên màn hình.
- [x] Map giá trị `yi` thành màu sắc (RGB hoặc HSL).
- [x] Tối ưu hóa việc vẽ hàng nghìn điểm mỗi giây.

## 5. Tương tác & UI
- [x] Thêm phím tắt để thay đổi Seed Matrix ngẫu nhiên (Phím `R`).
- [x] Thêm thanh trượt hoặc phím để điều chỉnh tốc độ Iteration (SPACE để pause).
- [ ] Thêm phím tăng/giảm `MOD_VALUE` (Phím `UP/DOWN`).
- [ ] Thêm phím nhập Seed Matrix/Mod từ console (Phím `C`).
- [x] Hiển thị thông tin ma trận hiện tại lên màn hình.

## 6. Đánh bóng & Hoàn thiện
- [ ] Thêm hiệu ứng mờ dần (Motion Blur) cho các điểm cũ (tùy chọn).
- [ ] Chụp ảnh màn hình kết quả (Phím `S`).
- [ ] Kiểm tra hiệu năng.

---
*Tiến độ: 0% hoàn thành*
