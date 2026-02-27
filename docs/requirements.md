# Tài liệu Yêu cầu Sản phẩm: Chaos Matrix - DDS Game

## 1. Tổng quan dự án
"Chaos Matrix" là một trò chơi/ứng dụng mô phỏng hình ảnh dựa trên **Hệ động lực rời rạc (Discrete Dynamical System - DDS)**. Ý tưởng cốt lõi là sử dụng các dãy số được tính toán từ các định thức ma trận để tạo ra các tọa độ và màu sắc trên màn hình, tạo nên một hiệu ứng "nhiễu có cấu trúc" (Chaos Game).

> [!NOTE]
> Trò chơi này không chỉ là một công cụ toán học mà còn là một trải nghiệm thị giác nghệ thuật (Generative Art).

## 2. Ý tưởng cốt lõi (Core Idea)
Dựa trên thuật toán trong `DDS.py`:
- **Tọa độ (x, y):** Sử dụng dãy `xi` và `xi+1` hoặc `xi` kết hợp với một biến số khác từ hệ thống để làm tọa độ vẽ điểm (pixel).
- **Màu sắc (Color):** Sử dụng dãy `yi` để quyết định màu sắc của điểm đó (ví dụ: gán cho giá trị Hue trong hệ HSL hoặc giá trị RGB).
- **Cấu trúc:** Mặc dù các con số nhìn có vẻ hỗn loạn (chaos), nhưng vì chúng tuân theo công thức định thức ma trận, các hình ảnh sinh ra sẽ có các vân hoặc cấu trúc ẩn (fractal-like).

## 3. Các tính năng chính (Key Features)

### 3.1. Mô phỏng thời gian thực (Real-time Simulation)
- Hệ thống sẽ liên tục tính toán các thế hệ tiếp theo (iterations) của dãy DDS.
- Vẽ các điểm lên màn hình ngay khi chúng được tính toán.

### 3.2. Tùy biến Ma trận Hạt giống (Seed Matrix Customization)
- Cho phép người chơi thay đổi 4 giá trị của `seed_matrix`. 
- Một sự thay đổi nhỏ trong hạt giống sẽ tạo ra một "vũ trụ" hình ảnh hoàn toàn khác biệt.

### 3.3. Điều khiển thông số (Parameter Control)
- **Tốc độ vẽ:** Tăng/giảm số lượng điểm vẽ mỗi khung hình.
- **Phạm vi (Modulus):** Sử dụng phép chia lấy dư (%) để giới hạn tọa độ trong kích thước màn hình và giới hạn màu sắc trong dải 0-255.

### 3.4. Chế độ màu sắc (Visual Modes)
- **Đơn sắc:** Chỉ sử dụng một màu với độ sáng khác nhau.
- **Cầu vồng:** Sử dụng dãy `yi` để chạy qua dải màu HSL.
- **Tương phản:** Sử dụng `op_det2` để đảo ngược màu sắc tại các vùng nhất định.

## 4. Công nghệ đề xuất
- **Ngôn ngữ:** Python.
- **Thư viện đồ họa:** 
  - `pygame` (cho tương tác thời gian thực và game-loop).
  - Hoặc `matplotlib` (nếu muốn thiên về phân tích đồ thị toán học).
- **Cơ chế toán học:** Kế thừa từ module `linear.det`.

## 5. Trải nghiệm người dùng (UX)
- Người dùng mở ứng dụng và thấy một màn hình đen.
- Các điểm sáng bắt đầu xuất hiện và kết nối lại thành các hình thù kỳ ảo.
- Người dùng có thể nhấn phím để "reset" với một ma trận ngẫu nhiên hoặc điều chỉnh bằng thanh trượt.

---
*Người soạn: Antigravity (Assistant)*
*Dành cho: Anh bạn đồng nghiệp của tôi.*
