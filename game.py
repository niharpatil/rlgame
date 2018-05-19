import sys, pygame
from player import Player
from heuristic_player import HeuristicPlayer
from AIAgent import AIAgent
import helpers
import numpy as np
import time

pygame.init()
pygame.display.init()

size = width, height = 100, 100

screen = pygame.display.set_mode(size)

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0, 0, 0)

player_width = 15
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

oldtime = time.time()
game = 1
games = []
def resetPositions(p1,p2):
  p1.x = width/2
  p2.x = width/2
  
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
  game_state = helpers.getGameStateArray(screen)
  move = p2.makeSmartMove(game_state)
  history = history + [(game_state[0], move)]

  if time.time() - oldtime >= 3:
    oldtime = time.time()
    history = history[:len(history) - 1]
    games = games + [(history, p1Hits)]
    # Train the neural network on batches of 20 games
    if game % 30 == 0:
      p2.trainOnEpisode(games, int(game/30))
      np.save("history/episode" + str(game/30), games)
      games = []
    history = []
    game += 1
    resetPositions(p1,p2)