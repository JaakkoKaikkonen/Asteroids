import pygame
import math

class Player:

    def __init__(self, x, y, radius):
        self.position = pygame.math.Vector2()
        self.position.x = x
        self.position.y = y
        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()
        self.radius = radius
        self.angle = 0
        self.angularVelocity = 0.05
        self.speed = 0.5
        self.dampening = 0.98

        self.vertices = [(-radius, radius), (0, -radius), (radius, radius)]
        self.transformedVertices = []


    def update(self, screen):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.velocity *= self.dampening
        self.acceleration.x = 0
        self.acceleration.y = 0

        if self.position.x - self.radius > screen.get_width():
            self.position.x = -self.radius
        elif self.position.x + self.radius < 0:
            self.position.x = screen.get_width() + self.radius

        if self.position.y - self.radius > screen.get_height():
            self.position.y = -self.radius
        elif self.position.y + self.radius < 0:
            self.position.y = screen.get_height() + self.radius

        self.transformedVertices.clear()
        for vertex in self.vertices:
            self.transformedVertices.append(((vertex[0] * math.cos(self.angle + math.pi / 2) + vertex[1] * -math.sin(self.angle + math.pi / 2)) + self.position.x,
                                             (vertex[0] * math.sin(self.angle + math.pi / 2) + vertex[1] * math.cos(self.angle + math.pi / 2)) + self.position.y))


    def spinLeft(self):
        self.angle -= self.angularVelocity

    def spinRight(self):
        self.angle += self.angularVelocity

    def move(self):
         self.acceleration.x = math.cos(self.angle) * self.speed
         self.acceleration.y = math.sin(self.angle) * self.speed

    def draw(self, screen):
        pygame.draw.lines(screen, (255, 255, 255), True, self.transformedVertices)

    def reset(self, x, y):
        self.position.x = x
        self.position.y = y
        self.velocity *= 0
        self.acceleration *= 0
        self.angle = 0