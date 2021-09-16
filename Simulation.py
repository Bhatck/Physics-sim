import sys
from random import random
import pygame
import math
from pygame.constants import DROPTEXT
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

def rotatevec(x, y, angle):
    return x*math.cos(angle)-y*math.sin(), y*math.sin(angle)+x*math.cos()

def distance(x1,y1,x2,y2):
  xd = x1-x2
  yd = y1-y2
  return math.sqrt(math.pow(xd,2)+math.pow(yd,2))    

def resolve_collision(particle1, particle2):
  dst = distance(particle1.x, particle1.y, particle2.x, particle2.y)
  #angle = math.atan2(ydiff, xdiff)
  #x, y = rotatevec(xdiff, ydiff, angle())
  #TODO Fix this thing
  if dst < particle1.radius + particle2.radius:
    return particle2.velocity
  else:
    return particle1.velocity

class Ball():
  def __init__(self, x, y, dx, dy,radius, color):
    self.x = x
    self.y = y
    self.velocity = [dx, dy]
    self.radius = radius
    self.color = color
  def update(self,particles):
    if self.y-self.radius<0 or self.y+self.radius>height:
      self.velocity[1] = -self.velocity[1]
    if self.x+self.radius>width or self.x-self.radius<0:
      self.velocity[0] = -self.velocity[0]
    self.x += self.velocity[0]
    self.y += self.velocity[1]
    for i in particles:
        if self != i:
            self.velocity = resolve_collision(self, i)
    
  def draw(self):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 10)

particles = []
for i in range(100):
  particles.append(Ball(random()*width,random()*height,random()-0.5*2,random()-0.5*2,10,(255,255,0)))
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  for particle in particles:
    particle.update(particles)
    #Draw all particles
    particle.draw()

  # Draw.

  pygame.display.flip()