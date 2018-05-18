import pygame

class Bullet:
  def __init__(self, x, y, screen, color, direction, velocity):
    self.x = x
    self.y = y
    self.screen = screen
    self.color = color
    self.direction = direction
    self.velocity = velocity
    self.rect = pygame.Rect(self.x, self.y, 5,5)

  def render(self):
    self.y = self.y - self.velocity if self.direction == "UP" else self.y + self.velocity
    self.rect = pygame.Rect(self.x, self.y, 3,3)
    pygame.draw.rect(self.screen, self.color, self.rect, 4)
  
  def getY(self):
    return self.y

  def getRect(self):
    return self.rect