import sys, pygame
from player import Player
from heuristic_player import HeuristicPlayer

pygame.init()
Surface = pygame.Surface

size = width, height = 500, 500
speed = [4, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

LEFT = 276
RIGHT = 275
SPACE = 32

RED = (255,0,0)
GREEN = (0,255,0)

player_width = 40
player_height = 10

p1_pos = 0
p2_pos = 0

velocity = 25

pygame.key.set_repeat(50, 50)

p1 = HeuristicPlayer(player_width, player_height, 5, 5, GREEN, screen, velocity)
p2 = Player(player_width, player_height, 0, height - player_height, RED, screen, velocity)

bullets = []

while 1:
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
 
    if keys[pygame.K_LEFT]:
      p2.move("LEFT")
    if keys[pygame.K_RIGHT]:
      p2.move("RIGHT")
    if keys[pygame.K_SPACE]:
      bullets = bullets + [p2.shoot("UP")]
  
  possibly_bullet = p1.makeSmartMove(p2, bullets)

  if possibly_bullet is not None:
    bullets = bullets + [possibly_bullet]

  screen.fill(black)
  p1.render()
  p2.render()

  for bullet in bullets:
    if bullet.getY() > height or bullet.getY() < 0:
      bullets.remove(bullet)
    bullet.render()

  pygame.display.flip()