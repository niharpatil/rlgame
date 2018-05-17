import pygame

class Bullet:
  def __init__(self, x, y, screen, color, direction, velocity):
    self.x = x
    self.y = y
    self.screen = screen
    self.color = color
    self.direction = direction
    self.velocity = velocity

  def render(self):
    self.y = self.y - self.velocity if self.direction == "UP" else self.y + self.velocity
    rect = (self.x, self.y, 5,5)
    pygame.draw.rect(self.screen, self.color, rect,2)
  
  def getY(self):
    return self.y