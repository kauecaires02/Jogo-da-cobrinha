# Jogo-da-cobrinha

import pygame, random
from pygame.locals import * 

def on_grid_random():
  x = random.randint(0, 590)
  y = random.randint(0, 590)
     return (x//10 * 10, y//10 * 10)

     def collision (c1, c2):
       return(c1[0] == c2[0]) and (c1[1] == C2[1])

UP = 0
RIGHT = 1
DOWN =2 
LEFT = 3

pygame.init()
scree = pygame.display.set_mode((600. 300))
pygame.diisplay.set_caption('snake')

snake = ([200. 200), (210.200), (200,200)]
snake_skinn = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0))

my_direction = LEFT 

clock = pygame.timr.Clock()

while True:
  clock.tick(2)

   for event in pygame.event.get():
       if event.type == QUIT:
         pygame.quit

      if event.type == KEYDOWN:

        if event.key == K_UP:
           my_direction = UP:

        if event.key == K_DOWN:
          my_direction = DOWN

        f event.key == K_LEFT:
           my_direction = LEFT

        if event.key == K_RIGHT:
          my direction  = RIGHT

if collision(snake[0], apples_pos):
    apple_pos = on_grid_random((0,0))

for i in range(len(snake) - 1, 0, -1):
    snake[i] = (snake[i][0], snake[i-1][1])

  if my_direction == UP:
    snake[0] = (snake[0][0], snake[0][1] - 10)
    if my direction == DOWN:

  snake[0] = (snake[0][0] + 10, snake[0][1] + 10)
    if my direction == RIGHT:

  snake[0] = (snake[0][0] - 10, snake[0][1] + 10)
    if my direction == LEFT:

  screen.fill((0,0,0))
  screen.blit(apple, apple_pos)
  for pos in snake:
    screen.blit(snake_skin,pos)
        
pygame.display update()


