import pygame
import random

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка ресурсов 
background = pygame.image.load(r"C:\Users\alinu\Documents\new_folder\labs\lab8\AnimatedStreet.png")
player_img = pygame.image.load(r"C:\Users\alinu\Documents\new_folder\labs\lab8\Player.png")
enemy_img = pygame.image.load(r"C:\Users\alinu\Documents\new_folder\labs\lab8\Enemy.png")
coin_img = pygame.image.load(r"C:\Users\alinu\Documents\new_folder\labs\lab8\coinn.png")
coin_img = pygame.transform.scale(coin_img, (50, 50))

# Музыка
pygame.mixer.music.load(r"C:\Users\alinu\Documents\new_folder\labs\lab8\Lectures_G1_Week10_racer_resources_background.wav")
crash_sound = pygame.mixer.Sound(r"C:\Users\alinu\Documents\new_folder\labs\lab8\Lectures_G1_Week10_racer_resources_crash.wav")

# Шрифты
score_font = pygame.font.SysFont("Verdana", 20)

# Переменные
PLAYER_SPEED = 5 #скорость игрока
ENEMY_SPEED = 4  #скорость врага
coin_count = 0   #счетчик для монеты
crash_count= 0  #счетчик для аварий

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(PLAYER_SPEED, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset()

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        """Сбрасываем врага в случайную позицию сверху"""
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h
        
    

player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    player.move()
    enemy.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    #проверяем если машина врежеться в враг
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        crash_count += 1  # Увеличиваем счетчик аварий
        enemy.reset()  # Перемещаем врага наверх
    
    # Отображение счёта аварий
    crash_text = score_font.render(f"Столкновение: {crash_count}", True, "white")
    screen.blit(crash_text, (11, 11))
    
    pygame.display.flip() 
    clock.tick(FPS)

pygame.quit()
