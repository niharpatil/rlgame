import pygame
from player import Player
from bullet import Bullet

shoot_frequency = 25

class HeuristicPlayer(Player):

  # may or not return Bullet depending on whether or not player decides to shoot
  def makeSmartMove(self, otherPlayer, bullets):
    if not hasattr(self,'bulletsShot'):
      self.bulletsShot = 0

    oX = otherPlayer.x

    # Want to avoid bullets at any cost
    filtered = [bullet for bullet in bullets if bullet.color!=self.color]
    bullets = [filtered[0]] if len(filtered) > 0 else []
    bullets = filtered[:2] if len(filtered) > 1 else []

    # If the bullet is going to hit us, we should avoid it
    if len(bullets) == 2:
      if bullets[0].x - bullets[1].x < 0 and bullets[0].x - 50 < self.x:
        self.move("LEFT")
      elif bullets[0].x - bullets[1].x > 0 and bullets[0].x + 50 > self.x:
        self.move("RIGHT")
      elif bullets[0].x - bullets[1].x == 0 and bullets[0].x - 50 < self.x: 
        self.move("LEFT") 
        
    elif len(bullets) == 1:
      if bullet and bullet.x + 50 >= self.x and bullet.x - 50 <= self.x + self.width:
          self.move("LEFT")
    # If not in danger of bullets, then go after player
    else:
      if self.x - oX < 0:
        self.move("RIGHT")
      elif self.x - oX > 0:
        self.move("LEFT")

    self.bulletsShot = self.bulletsShot + 1
    if self.bulletsShot % shoot_frequency == 0:
      return self.shoot("DOWN")

      