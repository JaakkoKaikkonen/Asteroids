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
        self.subAsteroidsVertexIndeces = []
        self.transformedVertices = []
        self.vertexCount = 15

        self.subAsteroidsVertexIndeces.append([])

        #Generate concave asteroid and split it into convex ones
        angle = 0
        vertexIndex = 0
        subAsteroidVertexIndex = 0
        while angle < (2 * math.pi):
            offsetX = random.random() * (radius * 0.5)
            offsetY = random.random() * (radius * 0.5)
            self.vertices.append((math.cos(angle) * self.radius + offsetX, math.sin(angle) * self.radius + offsetY))
            angle += (2 * math.pi) / self.vertexCount

            if subAsteroidVertexIndex < 2:
                self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(vertexIndex)
                subAsteroidVertexIndex += 1
            else:
                a = self.vertices[vertexIndex - 2]
                b = self.vertices[vertexIndex - 1]
                c = self.vertices[vertexIndex]

                area2 = ((b[0]-a[0])*(c[1]-a[1])) - ((b[1]-a[1])*(c[0]-a[0]))
                if area2 >= 0:
                    self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(vertexIndex)
                    subAsteroidVertexIndex += 1
                else:
                    self.subAsteroidsVertexIndeces.append([])
                    self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(vertexIndex - 1)
                    self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(vertexIndex)
                    subAsteroidVertexIndex = 2

            vertexIndex += 1

        #connect last one
        a = self.vertices[vertexIndex - 2]
        b = self.vertices[vertexIndex - 1]
        c = self.vertices[0]

        area2 = ((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0]))
        if area2 >= 0:
            self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(0)
        else:
            self.subAsteroidsVertexIndeces.append([])
            self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(vertexIndex - 1)
            self.subAsteroidsVertexIndeces[len(self.subAsteroidsVertexIndeces) - 1].append(0)


        self.transformedVertices.clear()
        for vertex in self.vertices:
            self.transformedVertices.append(vertex + self.position)


    def update(self, screen):
        self.position += self.velocity

        self.transformedVertices.clear()
        for vertex in self.vertices:
            self.transformedVertices.append(vertex + self.position)

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