import pygame
import math

class Bullet:

    def __init__(self, x, y, angle):
        self.position = pygame.math.Vector2()
        self.position.x = x
        self.position.y = y
        self.speed = 4
        self.velocity = pygame.math.Vector2()
        self.velocity.x = math.cos(angle) * self.speed
        self.velocity.y = math.sin(angle) * self.speed
        self.radius = 3

    def update(self):
        self.position += self.velocity

    def isOutOfScreen(self, screen):
        return (self.position.x - self.radius > screen.get_width() or self.position.x + self.radius < 0 or
                self.position.y - self.radius > screen.get_height() or self.position.y + self.radius < 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)