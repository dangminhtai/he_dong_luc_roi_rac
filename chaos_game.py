import pygame
import random
import sys
import colorsys
from linear.det import det2, op_det2

# Cấu hình màn hình
WIDTH, HEIGHT = 900, 900
FPS = 60
POINTS_PER_FRAME = 2000 
POINT_SIZE = 3          

class ChaosEngine:
    def __init__(self, seed_matrix=None, mod_value=2025):
        self.mod_value = mod_value
        self.reset(seed_matrix)

    def reset(self, seed_matrix=None):
        if seed_matrix is None:
            self.seed_matrix = [
                [random.randint(2, 500), random.randint(2, 500)],
                [random.randint(2, 500), random.randint(2, 500)]
            ]
        else:
            self.seed_matrix = seed_matrix
        
        self.result_matrix = [row.copy() for row in self.seed_matrix]
        self.iteration = 0
        self.last_pos = (0, 0)
        self.collapse_count = 0

    def next_point(self):
        try:
            new_matrix = [row[-2:] for row in self.result_matrix]
            
            xi = det2(new_matrix) % self.mod_value
            self.result_matrix[0].append(xi)
            
            yi_matrix = [
                [self.result_matrix[0][-2], xi],
                [self.result_matrix[1][-2], self.result_matrix[1][-1]]
            ]
            yi = op_det2(yi_matrix) % self.mod_value
            self.result_matrix[1].append(yi)
            
            self.iteration += 1
            
            x_plot = int(xi * WIDTH / self.mod_value)
            y_plot = int(yi * HEIGHT / self.mod_value)
            
            if (x_plot, y_plot) == self.last_pos:
                self.collapse_count += 1
            else:
                self.collapse_count = 0
            
            self.last_pos = (x_plot, y_plot)
            
            if self.collapse_count > 50:
                xi = (xi + random.randint(1, 10)) % self.mod_value
                yi = (yi + random.randint(1, 10)) % self.mod_value
                self.result_matrix[0].append(xi)
                self.result_matrix[1].append(yi)
                self.collapse_count = 0

            # Màu sắc
            hue = (xi / float(self.mod_value) + self.iteration * 0.001) % 1.0
            rgb = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
            color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
            
            return (x_plot, y_plot), color
        except Exception:
            self.reset(self.seed_matrix)
            return (WIDTH//2, HEIGHT//2), (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chaos Matrix - Pro Controller")
    font = pygame.font.SysFont("Consolas", 18)
    clock = pygame.time.Clock()
    
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill((20, 20, 25)) 
    
    # Khởi tạo với cấu hình hiện tại của anh
    current_seed = [[7, 3], [2, 1]]
    current_mod = 2025
    engine = ChaosEngine(current_seed, current_mod) 
    
    running = True
    paused = False
    
    print("\n--- VERSION 2.2: ĐIỀU KHIỂN NÂNG CAO ---")
    print("UP/DOWN: Tăng/Giảm Modulo (±10)")
    print("LEFT/RIGHT: Tăng/Giảm Modulo (±1)")
    print("C: Nhập Seed/Mod mới từ Terminal")
    print("R: Random Seed | S: Screenshot | SPACE: Pause")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    engine.reset()
                    canvas.fill((20, 20, 25))
                if event.key == pygame.K_s:
                    pygame.image.save(canvas, f"chaos_{engine.mod_value}_{engine.iteration}.png")
                    print("Đã lưu ảnh!")
                if event.key == pygame.K_SPACE:
                    paused = not paused
                
                # Điều chỉnh Modulo
                if event.key == pygame.K_UP:
                    engine.mod_value += 10
                    engine.reset(engine.seed_matrix)
                    canvas.fill((20, 20, 25))
                if event.key == pygame.K_DOWN:
                    engine.mod_value = max(1, engine.mod_value - 10)
                    engine.reset(engine.seed_matrix)
                    canvas.fill((20, 20, 25))
                if event.key == pygame.K_RIGHT:
                    engine.mod_value += 1
                    engine.reset(engine.seed_matrix)
                    canvas.fill((20, 20, 25))
                if event.key == pygame.K_LEFT:
                    engine.mod_value = max(1, engine.mod_value - 1)
                    engine.reset(engine.seed_matrix)
                    canvas.fill((20, 20, 25))
                
                # Nhập từ terminal
                if event.key == pygame.K_c:
                    print("\n--- NHẬP THÔNG SỐ MỚI ---")
                    try:
                        new_mod = int(input("Nhập MOD_VALUE mới (mặc định 2025): ") or engine.mod_value)
                        print("Nhập ma trận 2x2 (ví dụ: 7 3 2 1):")
                        raw_mat = input().split()
                        if len(raw_mat) == 4:
                            new_seed = [
                                [int(raw_mat[0]), int(raw_mat[1])],
                                [int(raw_mat[2]), int(raw_mat[3])]
                            ]
                            engine.mod_value = new_mod
                            engine.reset(new_seed)
                            canvas.fill((20, 20, 25))
                            print(f"Đã cập nhật: Mod={new_mod}, Seed={new_seed}")
                    except ValueError:
                        print("Lỗi định dạng, vui lòng nhập số!")

        if not paused:
            for _ in range(POINTS_PER_FRAME):
                pos, color = engine.next_point()
                pygame.draw.rect(canvas, color, (pos[0], pos[1], POINT_SIZE, POINT_SIZE))

        screen.blit(canvas, (0, 0))
        
        # UI Overlay rực rỡ
        color_val = (0, 255, 100)
        overlay1 = font.render(f"MOD: {engine.mod_value} (Arrows to change)", True, color_val)
        overlay2 = font.render(f"SEED: {engine.seed_matrix} (C to edit)", True, color_val)
        overlay3 = font.render(f"POINTS: {engine.iteration}", True, color_val)
        
        screen.blit(overlay1, (10, HEIGHT - 80))
        screen.blit(overlay2, (10, HEIGHT - 55))
        screen.blit(overlay3, (10, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
