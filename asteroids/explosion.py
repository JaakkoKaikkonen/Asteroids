import pygame
import math

class Explosion:

    def __init__(self, x, y, particleCount, lifeTime):
        self.middle = pygame.math.Vector2()
        self.middle.x = x
        self.middle.y = y
        self.positions = []
        self.velocities = []
        self.speed = 2
        self.radius = 1
        self.intensity = 255
        self.lifeTime = lifeTime
        self.lifeTimer = lifeTime
        self.particleCount = particleCount

        angle = 0
        while angle < (2 * math.pi):
            self.velocities.append((math.cos(angle) * self.speed, math.sin(angle) * self.speed))
            angle += (2 * math.pi) / self.particleCount

        for i in range(self.particleCount):
            self.positions.append(pygame.math.Vector2())
            self.positions[i].x = self.middle.x
            self.positions[i].y = self.middle.y


    def update(self):
        self.lifeTimer -= 1
        self.intensity = self.map(self.lifeTimer, 0, self.lifeTime, 0, 255)
        for i in range(self.particleCount):
          self.positions[i] += self.velocities[i]

    def draw(self, screen):
        for i in range(self.particleCount):
            pygame.draw.circle(screen, (self.intensity, self.intensity, self.intensity), (int(self.positions[i].x), int(self.positions[i].y)), self.radius)

    def map(self, value, min1, max1, min2, max2):
        return ((value - min1) / (max1 - min1)) * (max2 - min2) + min2