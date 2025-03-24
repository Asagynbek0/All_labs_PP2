import pygame
import os
import time

from datetime import datetime
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
clock = pygame.time.Clock()
image = get_image('min_hand.png').get_rect()


min_o=45
sec_o= -60
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('clock.png'), (0, 0))
        
        now=datetime.now()
        sec=now.second
        min=now.minute
        
        angle_s= -(sec*6 + sec_o)
        angle_m = -(min * 6 + min_o)

        clock_center = (400, 300)
        rotated_minute = pygame.transform.rotate(get_image('min_hand.png'), angle_m)
        rotated_sec = pygame.transform.rotate(get_image('sec_hand.png'), angle_s)

      
        rotated_m = rotated_minute.get_rect(center=clock_center)
        rotated_s = rotated_sec.get_rect(center=clock_center)

        screen.blit(rotated_minute, rotated_m)
        screen.blit(rotated_sec, rotated_s)
        
        pygame.display.flip()
        clock.tick(1)