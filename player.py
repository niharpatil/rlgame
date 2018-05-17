import pygame
from bullet import Bullet

class Player:
  def __init__(self, width, height, x, y, color, screen, velocity):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.color = color
    self.screen = screen
    self.velocity = velocity

  def render(self):
    rect_body = (self.x, self.y, self.width, self.height)
    pygame.draw.rect(self.screen, self.color, rect_body, 1)
    rect_gun = (2*self.x + self.width)/2 - 1, self.y, 2, self.height
    pygame.draw.rect(self.screen, self.color, rect_gun, 2)

  def move(self,direction):
    if direction == "LEFT":
      self.x = max(0, self.x - self.velocity)
    else:
      self.x = min(self.screen.get_width() - self.width, self.x + self.velocity)
  
  def shoot(self, direction):
    bulletX = (2*self.x + self.width)/2 - 1
    return Bullet(bulletX, self.y, self.screen, self.color, direction, 10)
    