# Hệ động lực rời rạc (Discrete Dynamical System)

# 1 ma trận vuông mô phỏng x0,x1,y0,y1

from linear.det import det2, op_det2
seed_matrix = [[7, 2],
               [3, 1]]

# Thêm cặp vector (x0,y0) và (x1,y1) vào ma trận result_matrix
result_matrix = seed_matrix.copy()

LOOP = 10
if __name__ == "__main__":
    for i in range(LOOP):
        # Lấy 2 cột cuối cùng của ma trận result_matrix để tính xi và yi
        new_matrix = [row[len(result_matrix[0])-2:] for row in result_matrix]

        xi = det2(new_matrix)
        # xi = xi % 2025  # Lấy phần dư của xi khi chia cho 2025
        result_matrix[0].append(xi)
        yi = op_det2([[result_matrix[0][i+1], xi],
                      [result_matrix[1][i], result_matrix[1][i+1]]])
        # yi = yi % 2025  # Lấy phần dư của yi khi chia cho 2025
        result_matrix[1].append(yi)
    print(result_matrix)
