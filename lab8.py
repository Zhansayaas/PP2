import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
pygame.init()

# Инициализация размеров окна
W, H = 800, 600


# Начальный масштаб и центр фрактала
scale = 200.0
center_x, center_y = 0.0, 0.0

# Создание окна Pygame
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Zooming Fractal")
sc.fill(WHITE)

# Флаг для изменения цвета фрактала
color_change = False
current_palette_index = 0 
# Функция для пересчета масштаба и центра фрактала при изменении масштаба
def update_fractal(mouse_x, mouse_y, zoom_in):
    global scale, center_x, center_y

    if zoom_in:
        # Увеличение масштаба при нажатии левой кнопки мыши
        scale *= 1.1
    else:
        # Уменьшение масштаба при нажатии правой кнопки мыши
        scale /= 1.1

    # Пересчет центра фрактала в соответствии с новым масштабом
    center_x += (mouse_x - W / 2) / scale
    center_y += (mouse_y - H / 2) / scale

# Функция для рисования фрактала Мандельброта
def draw_fractal():
    sc.fill(WHITE)
    max_iter = 100
    
    for y in range(H):
        for x in range(W):
            current_palette_index=0
            # Пересчет координат в комплексную плоскость
            a = (x - W / 2) / scale + center_x
            b = (y - H / 2) / scale + center_y
            c = complex(a, b)
            z = 0
            n = 0

            while abs(z) <= 2 and n < max_iter:
                z = z * z + c
                n += 1

            if n == max_iter:
                color = BLACK
            else:
                color_palettes = [(n % 32 * 8, n % 16 * 16, n % 4 * 32), (n % 32 * 8, n % 16 * 16, n % 2 * 32), (n % 32 * 8, n % 16 * 16, n % 4 * 20)]
                
                if color_change:
                    current_palette_index+=1
                    color = color_palettes[current_palette_index]
                    
                else:
                    color = (n % 32 * 8, n % 16 * 16, n % 8 * 32)

            pygame.draw.circle(sc, color, (x, y), 1)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши для увеличения масштаба (приближения)
                update_fractal(event.pos[0], event.pos[1], True)
                draw_fractal()
            elif event.button == 3:  # Правая кнопка мыши для уменьшения масштаба (отдаления)
                update_fractal(event.pos[0], event.pos[1], False)
                draw_fractal()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:  # Нажата кнопка "B" для изменения цвета фрактала
                color_change = not color_change  # Переключение флага изменения цвета
                draw_fractal()

    pygame.display.update()

pygame.quit()
