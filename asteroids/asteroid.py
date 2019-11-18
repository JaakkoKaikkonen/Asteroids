import pygame
import math
import random

class Asteroid:

    def __init__(self, x, y, radius):
        self.position = pygame.math.Vector2()
        self.position.x = x
        self.position.y = y
        self.radius = radius
        self.speed = 2
        self.velocity = pygame.math.Vector2()
        self.velocity.x = (random.randrange(0, 1000) - 500) / 1000 * self.speed
        self.velocity.y = (random.randrange(0, 1000) - 500) / 1000 * self.speed

        self.vertices = []
        self.transformedVertices = []
        self.vertexCount = 15

        angle = 0
        while angle < (2 * math.pi):
            offsetX = random.random() * (radius * 0.5)
            offsetY = random.random() * (radius * 0.5)
            self.vertices.append((math.cos(angle) * self.radius + offsetX, math.sin(angle) * self.radius + offsetY))
            angle += (2 * math.pi) / self.vertexCount

        self.transformedVertices.clear()
        for vertex in self.vertices:
            self.transformedVertices.append(vertex + self.position)


    def update(self, screen):
        self.transformedVertices.clear()
        for vertex in self.vertices:
            self.transformedVertices.append(vertex + self.position)

        self.position += self.velocity

        if self.position.x - self.radius > screen.get_width():
            self.position.x = -self.radius
        elif self.position.x + self.radius < 0:
            self.position.x = screen.get_width() + self.radius

        if self.position.y - self.radius > screen.get_height():
            self.position.y = -self.radius
        elif self.position.y + self.radius < 0:
            self.position.y = screen.get_height() + self.radius

    def draw(self, screen):
        pygame.draw.lines(screen, (255, 255, 255), True, self.transformedVertices)