import pygame
import random
from color_palette import *

pygame.init()

# Размер окна и ячейки
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки (для змейки и еды)
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Класс змейки
class Snake:
  def __init__(self):
    self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
    self.dx, self.dy = 1, 0  # Направление движения
    self.grow = False  # Флаг для роста змейки

  def move(self):
    if self.grow:
      self.body.append(Point(self.body[-1].x, self.body[-1].y))
      self.grow = False
    
    # Перемещение тела змейки
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i].x = self.body[i - 1].x
      self.body[i].y = self.body[i - 1].y

    # Двигаем голову змейки
    self.body[0].x += self.dx
    self.body[0].y += self.dy

  def draw(self):
    pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
    for segment in self.body[1:]:
      pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

  def check_collision(self, food):
    if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
      self.grow = True  # Увеличиваем змейку
      return True
    return False

  def check_self_collision(self):
    head = self.body[0]
    return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

  def check_wall_collision(self):
    head = self.body[0]
    return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

# Класс еды
class Food:
  def __init__(self):
    self.food_types = [
      {"color": colorGREEN, "weight": 70},  # Обычная еда (чаще)
      {"color": colorBLUE, "weight": 20},   # Средняя редкость
      {"color": colorYELLOW, "weight": 10}  # Редкая еда (реже)
    ]
    self.spawn_time = pygame.time.get_ticks()  # Время появления еды
    self.lifetime = random.randint(3000, 7000)  # Живет от 3 до 7 секунд
    self.randomize()
    

  def randomize(self):
    chosen_food = random.choices(self.food_types, weights=[f["weight"] for f in self.food_types])[0]
    self.color = chosen_food["color"]
    self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
    self.spawn_time = pygame.time.get_ticks()  # Обновляем время появления
    self.lifetime = random.randint(3000, 7000)  # Новое случайное время жизни

  def is_expired(self):
    return pygame.time.get_ticks() - self.spawn_time > self.lifetime

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
# Отображение текста (счёт и уровень)
def draw_text(text, x, y, color):
  font = pygame.font.Font(None, 36)
  surface = font.render(text, True, color)
  screen.blit(surface, (x, y))

# Инициализация игры
FPS = 5
score = 0
level = 1
clock = pygame.time.Clock()
food = Food()
snake = Snake()

game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, "red")

running = True
while running:
  screen.fill(colorBLACK)  # Очищаем экран
  draw_grid_chess()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT and snake.dx == 0:
        snake.dx, snake.dy = 1, 0
      elif event.key == pygame.K_LEFT and snake.dx == 0:
        snake.dx, snake.dy = -1, 0
      elif event.key == pygame.K_DOWN and snake.dy == 0:
        snake.dx, snake.dy = 0, 1
      elif event.key == pygame.K_UP and snake.dy == 0:
        snake.dx, snake.dy = 0, -1

  snake.move()
  
  # Проверяем на столкновение с собой или со стеной
  if snake.check_self_collision() or snake.check_wall_collision():
    screen.fill(colorBLACK)
    center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over, center_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    running = False
    continue

  if snake.check_collision(food):
    if food.color == colorGREEN:
        score += 1  # Увеличиваем очки если сьедает
    if food.color == colorBLUE:
        score += 2
    if food.color == colorYELLOW:
        score += 3
    food.randomize()
    
  if food.is_expired():
    food.randomize()
    
    # Повышение уровня каждые 4 очка
    if score % 4 == 0:
      level += 1
      FPS += 1  # Увеличиваем скорость игры

  # Рисуем объекты
  snake.draw()
  food.draw()
  draw_text(f"Score: {score}", 10, 10, colorBLACK)
  draw_text(f"Level: {level}", 10, 40, colorBLACK)
  
  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()