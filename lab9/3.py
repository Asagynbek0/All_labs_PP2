import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Цвета
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)

# Начальные параметры
screen.fill(colorBLACK)
LMBpressed = False
RMBpressed = False
THICKNESS = 5
mode = "brush"  # brush (кисть), rect (прямоугольник), circle (круг)
prevX = prevY = 0
startX = startY = 0
rect = pygame.Rect(0, 0, 0, 0)
circle = pygame.Rect(0, 0, 0, 0)
rects = []  # Храним нарисованные фигуры
circles = []
squares = []
r_triangles = []
r_triangle = [] 
e_triangles = []
e_triangle = []
rhombuses = []
rhombuse = []
drawing_surface = screen.copy()
curr_color = colorRED  # Выбранный цвет
clock = pygame.time.Clock()

done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        mode = "brush"
      elif event.key == pygame.K_2:
        mode = "rect"
      elif event.key == pygame.K_3:
        mode = "circle"
      elif event.key == pygame.K_4:
        mode = "square"
      elif event.key == pygame.K_5:
        mode = "r_triangle"
      elif event.key == pygame.K_6:
        mode = "e_triangle"
      elif event.key == pygame.K_7:
        mode = "rhombus"
      elif event.key == pygame.K_EQUALS:
        THICKNESS += 1
      elif event.key == pygame.K_MINUS:
        THICKNESS = max(1, THICKNESS - 1)
      elif event.key == pygame.K_c:
        screen.fill(colorBLACK)
        rects.clear()
        circles.clear()
        r_triangles.clear()
        squares.clear()
        e_triangles.clear()
        rhombuses.clear()
        drawing_surface = screen.copy()
      elif event.key == pygame.K_r:
        curr_color = colorRED
      elif event.key == pygame.K_g:
        curr_color = colorGREEN
      elif event.key == pygame.K_b:
        curr_color = colorBLUE
    
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Левая кнопка (рисование)
        LMBpressed = True
        prevX, prevY = event.pos
        if mode == "rect":
          startX, startY = event.pos
          rect = pygame.Rect(startX, startY, 0, 0)
        elif mode == "circle":
          startX, startY = event.pos
          circle = pygame.Rect(startX, startY, 0, 0)
        elif mode == "square":
          startX, startY = event.pos
          square = pygame.Rect(startX, startY, 0, 0)
        elif mode == "r_triangle":
          startX, startY = event.pos
          r_triangle = [(startX, startY), (startX, startY), (startX, startY)]
        elif mode == "e_triangle":
          startX, startY = event.pos
          e_triangle = [(startX, startY), (startX, startY), (startX, startY)]
        elif mode == "rhombus":
          startX, startY = event.pos
          rhombuse = pygame.Rect(startX, startY, 0, 0)
      elif event.button == 3:  # Правая кнопка (ластик)
        RMBpressed = True
        prevX, prevY = event.pos
    
    elif event.type == pygame.MOUSEMOTION:
      currX, currY = event.pos
      if LMBpressed and mode == "brush":
        pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY
      elif LMBpressed and mode == "rect":
        rect.x = min(startX, currX)
        rect.y = min(startY, currY)
        rect.width = abs(currX - startX)
        rect.height = abs(currY - startY)
      elif LMBpressed and mode == "circle":
        radius = max(abs(currX - startX), abs(currY - startY)) // 2
        circle.x = startX - radius
        circle.y = startY - radius
        circle.width = circle.height = radius * 2
      elif LMBpressed and mode == "square":
        square.x = min(startX, currX)
        square.y = min(startY, currY)
        square.width = abs(currX - startX)
        square.height = abs(currX - startX)
      elif LMBpressed and mode == "r_triangle":
        r_triangle = [(currX, currY), (startX, startY), (startX, currY)]  # Левый нижний угол, Левый верхний угол, Правый нижний угол
      elif LMBpressed and mode == "e_triangle":
        side = abs(currX - startX)  # Длина стороны
        height = (math.sqrt(3) / 2) * side  # Высота треугольника  
        e_triangle = [
            (startX, startY),  # Первая вершина (начало)
            (startX + side, startY),  # Вторая вершина (по горизонтали)
            (startX + side / 2, startY - height)  # Третья вершина (вверх)
        ]
      elif LMBpressed and mode == "rhombus":
        centerX = (startX + currX) // 2
        centerY = (startY + currY) // 2
        width = abs(currX - startX)
        height = abs(currY - startY)
        rhombus = [
          (centerX - width // 2, centerY),  # Левая вершина
          (centerX, centerY - height // 2), # Верхняя вершина
          (centerX + width // 2, centerY),  # Правая вершина
          (centerX, centerY + height // 2)  # Нижняя вершина
        ]
      elif RMBpressed:  # Ластик
        pygame.draw.line(drawing_surface, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY
    
    elif event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
        LMBpressed = False
        if mode == "rect":
          rects.append((rect.copy(), curr_color))  # Сохраняем прямоугольник
        elif mode == "circle":
          circles.append((circle.copy(), curr_color))  # Сохраняем круг
        elif mode == "square":
          squares.append((square.copy(), curr_color))
        elif mode == "r_triangle" and len(r_triangle) == 3:
          r_triangles.append((r_triangle.copy(), curr_color))  # Сохраняем треугольник
        elif mode == "e_triangle" and len(e_triangle) == 3:
          e_triangles.append((e_triangle.copy(), curr_color))  # Сохраняем треугольник
        elif mode == "rhombus" and len(rhombus) == 4:
          rhombuses.append((rhombus.copy(), curr_color))
      elif event.button == 3:
        RMBpressed = False

  # Перерисовываем экран
  screen.blit(drawing_surface, (0, 0))
  for r, color in rects:
    pygame.draw.rect(screen, color, r, 2)
  for c, color in circles:
    pygame.draw.ellipse(screen, color, c, 2)
  for s, color in squares:
    pygame.draw.rect(screen, color, s, 2)
  for r, color in r_triangles:
    pygame.draw.polygon(screen, color, r, 2)
  for e, color in e_triangles:
    pygame.draw.polygon(screen, color, e, 2)
  for rh, color in rhombuses:
    pygame.draw.polygon(screen, color, rh, 2)

  # Отображаем текущую фигуру
  if LMBpressed and mode == "rect":
    pygame.draw.rect(screen, curr_color, rect, 2)
  elif LMBpressed and mode == "circle":
    pygame.draw.ellipse(screen, curr_color, circle, 2)
  elif LMBpressed and mode == "square":
    pygame.draw.rect(screen, curr_color, square, 2)
  elif LMBpressed and mode == "r_triangle" and len(r_triangle) == 3:
    pygame.draw.polygon(screen, curr_color, r_triangle, 2)
  elif LMBpressed and mode == "e_triangle" and len(e_triangle) == 3:
    pygame.draw.polygon(screen, curr_color, e_triangle, 2)
  elif LMBpressed and mode == "rhombus" and len(rhombuse) == 4:
    pygame.draw.rect(screen, curr_color, rhombuse, 2)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()