import pygame

playlist = [r"C:\Users\alinu\Documents\new_folder\labs\Wake Up In The Sky.mp3",r"C:\Users\alinu\Documents\new_folder\labs\De Lacure - Qsh.mp3"]
current_track = 0

def play():
  pygame.mixer.music.load(playlist[current_track])
  pygame.mixer.music.play(-1)
  print(f"Playing")
  
def stop():
  pygame.mixer.music.stop()
  print("Music stopped")

def next():
  global current_track
  current_track = (current_track + 1) % len(playlist)
  play()

def previous():
  global current_track
  current_track = (current_track - 1) % len(playlist)
  play()

pygame.init()
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200, 200))

while not done:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill((255, 255, 255))
  pressed = pygame.key.get_pressed() 
  if pressed[pygame.K_SPACE]: stop() #stop
  if pressed[pygame.K_0]: play() #play
  if pressed[pygame.K_RIGHT]: next() #next
  if pressed[pygame.K_LEFT]: previous() #previous

  pygame.display.flip()