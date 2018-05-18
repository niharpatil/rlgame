import sys, pygame
from player import Player
from heuristic_player import HeuristicPlayer
from AIAgent import AIAgent
import helpers
import numpy as np

pygame.init()
pygame.display.init()

size = width, height = 100, 100

screen = pygame.display.set_mode(size)

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0, 0, 0)

player_width = 20
player_height = 10

p1_pos = width/2
p2_pos = width/2

velocity = 25

pygame.key.set_repeat(50, 50)

p1 = HeuristicPlayer(player_width, player_height, p1_pos, 0, GREEN, screen, velocity)
p2 = AIAgent(player_width, player_height, p2_pos, height - player_height, RED, screen, velocity)

#AI CODE
p2.setupNet()

bullets = []

p1Hits = 0
p2Hits = 0
  
history = []

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

  screen.fill(BLACK)
  p1.render()
  p2.render()

  for bullet in bullets:
    if bullet.getY() > height or bullet.getY() < 0:
      bullets.remove(bullet)
      break
    if (bullet.color != p2.color and p2.isShot(bullet)):
      p1Hits += 1
      bullets.remove(bullet)
      break
    if (bullet.color != p1.color and p1.isShot(bullet)):
      p2Hits += 1
      bullets.remove(bullet)
      break
    bullet.render()

  pygame.display.flip()
  history = history + [helpers.getGameStateArray(screen)]
  p2.makeSmartMove(history[-1])
  
  if p1Hits >= 3 or p2Hits >= 3:
    history = history[:len(history) - 1]
    np.save("history", history)
    sys.exit()