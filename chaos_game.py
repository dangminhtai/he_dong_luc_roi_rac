import pygame
import random
import sys
import colorsys
from linear.det import det2, op_det2

# Cấu hình
FPS = 60

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

    def next_point(self, width, height):
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
            
            x_plot = int(xi * width / self.mod_value)
            y_plot = int(yi * height / self.mod_value)
            
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
            return (width//2, height//2), (255, 255, 255)

def draw_text(surface, text, font, color, x, y):
    obj = font.render(text, True, color)
    surface.blit(obj, (x, y))

def main():
    pygame.init()
    # FULL SCREEN trực tiếp, tự lấy kích thước chuẩn của hệ điều hành
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    W, H = screen.get_size()
    pygame.display.set_caption("Chaos Matrix - Ultimate Edition")
    font = pygame.font.SysFont("Consolas", 24)
    big_font = pygame.font.SysFont("Consolas", 48, bold=True)
    clock = pygame.time.Clock()
    
    canvas = pygame.Surface((W, H))
    canvas.fill((15, 15, 20)) 
    
    # State quản lý UI in-game
    state = "MENU" # Có thể là "MENU" hoặc "PLAYING"
    
    # Input field vars
    inputs = ["2024", "7 3 2 1", "2000"]
    active_field = 0
    prompts = ["MOD_VALUE:", "SEED (4 số cách nhau):", "SPEED (Điểm/frame):"]
    
    engine = None
    points_per_frame = 2000
    point_size = 3
    paused = False
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Trong game bấm ESC để ra menu, ở menu bấm ESC để thoát
                    if state == "PLAYING":
                        state = "MENU"
                    else:
                        running = False
                        
                if state == "MENU":
                    if event.key == pygame.K_UP:
                        active_field = max(0, active_field - 1)
                    elif event.key == pygame.K_DOWN:
                        active_field = min(len(inputs) - 1, active_field + 1)
                    elif event.key == pygame.K_RETURN:
                        # Parse và Start Game
                        try:
                            mod_val = int(inputs[0]) if inputs[0].strip() else 2025
                            raw_mat = inputs[1].split()
                            if len(raw_mat) == 4:
                                seed_mat = [[int(raw_mat[0]), int(raw_mat[1])], [int(raw_mat[2]), int(raw_mat[3])]]
                            else:
                                seed_mat = [[7, 3], [2, 1]]
                            points_per_frame = int(inputs[2]) if inputs[2].strip() else 2000
                            
                            engine = ChaosEngine(seed_mat, mod_val)
                            canvas.fill((15, 15, 20))
                            state = "PLAYING"
                            paused = False
                        except ValueError:
                            pass # Bỏ qua nếu nhập bậy bạ
                            
                    elif event.key == pygame.K_BACKSPACE:
                        inputs[active_field] = inputs[active_field][:-1]
                    else:
                        # Chỉ cho phép gõ số, khoảng trắng hoặc dấu trừ
                        if event.unicode.isdigit() or event.unicode in [' ', '-']:
                            inputs[active_field] += event.unicode
                            
                elif state == "PLAYING":
                    if event.key == pygame.K_r:
                        engine.reset()
                        canvas.fill((15, 15, 20))
                    elif event.key == pygame.K_s:
                        pygame.image.save(canvas, f"chaos_mtx_{engine.mod_value}_{engine.iteration}.png")
                    elif event.key == pygame.K_SPACE:
                        paused = not paused
                    elif event.key == pygame.K_c or event.key == pygame.K_m:
                        state = "MENU" # Về lại màn hình menu để nhập
                    
                    # Chỉnh Speed On-the-fly
                    elif event.key == pygame.K_RIGHTBRACKET:
                        points_per_frame += 100
                    elif event.key == pygame.K_LEFTBRACKET:
                        points_per_frame = max(1, points_per_frame - 100)
                        
                    # Chỉnh Modulo On-the-fly
                    elif event.key == pygame.K_UP:
                        engine.mod_value += 10
                        engine.reset(engine.seed_matrix)
                        canvas.fill((15, 15, 20))
                    elif event.key == pygame.K_DOWN:
                        engine.mod_value = max(1, engine.mod_value - 10)
                        engine.reset(engine.seed_matrix)
                        canvas.fill((15, 15, 20))
                    elif event.key == pygame.K_RIGHT:
                        engine.mod_value += 1
                        engine.reset(engine.seed_matrix)
                        canvas.fill((15, 15, 20))
                    elif event.key == pygame.K_LEFT:
                        engine.mod_value = max(1, engine.mod_value - 1)
                        engine.reset(engine.seed_matrix)
                        canvas.fill((15, 15, 20))

        # Logic Update & Draw
        if state == "MENU":
            screen.fill((30, 30, 40))
            draw_text(screen, "CHAOS MATRIX SETTINGS", big_font, (0, 255, 150), 50, 50)
            
            draw_text(screen, "Điền thông số và nhấn ENTER để chạy hình, ESC để thoát.", font, (200, 200, 200), 50, 120)
            
            y_offset = 200
            for i, prompt in enumerate(prompts):
                color = (255, 255, 0) if i == active_field else (150, 150, 150)
                draw_text(screen, prompt, font, color, 50, y_offset)
                
                # Vẽ khung dỏm
                pygame.draw.rect(screen, color, (350, y_offset - 5, 400, 35), 2)
                draw_text(screen, inputs[i] + ("_" if i == active_field else ""), font, (255, 255, 255), 360, y_offset)
                
                y_offset += 70
                
            draw_text(screen, "Trò chơi hỗ trợ: Mũi tên (chọn dòng), Nhập Số, Backspace, Enter.", font, (100, 100, 100), 50, H - 50)
            pygame.display.flip()
            clock.tick(30)
            
        elif state == "PLAYING":
            if not paused and engine:
                for _ in range(points_per_frame):
                    pos, color = engine.next_point(W, H) # Truyền W, H vào
                    pygame.draw.rect(canvas, color, (pos[0], pos[1], point_size, point_size))

            screen.blit(canvas, (0, 0))
            
            # UI Overlay
            color_u = (0, 255, 150)
            draw_text(screen, f"MOD: {engine.mod_value} (Chỉnh bằng phím Mũi Tên)", font, color_u, 20, H - 120)
            draw_text(screen, f"SEED: {engine.seed_matrix}", font, color_u, 20, H - 90)
            draw_text(screen, f"SPEED: {points_per_frame} pts/frame (Chỉnh bằng phím [ và ])", font, color_u, 20, H - 60)
            draw_text(screen, f"Phím tắt: ESC: Menu | SPACE: Dừng/Chạy | R: Random | S: Lưu Hình", font, (255, 255, 255), 20, H - 30)

            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
