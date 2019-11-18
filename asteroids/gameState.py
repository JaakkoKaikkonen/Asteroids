import pygame
import random

from asteroid import *
from player import *
from collision import *
from bullet import *
from explosion import *

class GameState:

    def __init__(self, screen):
        self.player = Player(screen.get_width() / 2, screen.get_height() / 2, 30)

        self.bullets = []

        self.explosions = []

        self.shootTime = 20
        self.shootTimer = 20

        self.gameOver = False
        self.gameOverTime = 200
        self.gameOverTimer = 0

        self.win = False

        self.score = 0

        fontName = pygame.font.match_font('arial')
        self.font1 = pygame.font.Font(fontName, 52)
        self.gameOverTextSurface = self.font1.render("Game over", True, (255, 255, 255))
        self.gameOvertextRect = self.gameOverTextSurface.get_rect()
        self.gameOvertextRect.midtop = (screen.get_width() / 2, screen.get_height() * 0.25)

        self.renderScoreToSurface()
        self.scoreTextRect = self.scoreTextSurface.get_rect()
        self.scoreTextRect.left = 20
        self.scoreTextRect.top = 20

        self.font2 = pygame.font.Font(fontName, 72)
        self.winTextSurface = self.font2.render("Win", True, (255, 255, 255))
        self.winTextRect = self.winTextSurface.get_rect()
        self.winTextRect.midtop = (screen.get_width() / 2, screen.get_height() * 0.25)

        self.asteroids = []
        self.numberOfAsteroids = 15
        self.spawnAsteroids(screen)



    def handleInput(self, screen):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r] and (self.win or self.gameOver):
            self.restart(screen)

        if not self.gameOver:

            if keys[pygame.K_LEFT]:
                self.player.spinLeft()
            if keys[pygame.K_RIGHT]:
                self.player.spinRight()
            if keys[pygame.K_UP]:
                self.player.move()

            self.shootTimer += 1
            if keys[pygame.K_SPACE] and self.shootTimer > self.shootTime:
                self.shootTimer = 0
                self.shoot()


    def update(self, screen):

        if self.gameOver:

            self.gameOverTimer += 1
            if self.gameOverTimer > self.gameOverTime:
                self.restart(screen)

        else:

            #Asteroid player collision
            for asteroid in self.asteroids:
                if circleCollision(asteroid.position.x, asteroid.position.y, asteroid.radius, self.player.position.x, self.player.position.y, self.player.radius * 0.7):
                    self.explosions.append(Explosion(self.player.position.x, self.player.position.y, 18, 120))
                    self.gameOver = True

            # Asteroid bullet collision
            for asteroid in self.asteroids:
               for bullet in self.bullets:
                   if circleCollision(asteroid.position.x, asteroid.position.y, asteroid.radius, bullet.position.x, bullet.position.y, bullet.radius):
                       if asteroid.radius > 20:
                            self.asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                            self.asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))

                       self.explosions.append(Explosion(asteroid.position.x, asteroid.position.y, 12, 50))
                       self.asteroids.remove(asteroid)
                       self.bullets.remove(bullet)
                       #Increse score
                       self.score += 10
                       self.renderScoreToSurface()
                       break

            #Delete bullets that are out of screen
            for bullet in self.bullets:
                if bullet.isOutOfScreen(screen):
                    self.bullets.remove(bullet)

            #Update player
            self.player.update(screen)

            #Update asteroids
            for asteroid in self.asteroids:
                asteroid.update(screen)

            # Update bullets
            for bullet in self.bullets:
                bullet.update()

            if len(self.asteroids) == 0:
                self.win = True
                offSetX = math.cos(self.player.angle + math.pi) * self.player.radius
                offSetY = math.sin(self.player.angle + math.pi) * self.player.radius
                self.explosions.append(Explosion(self.player.position.x + offSetX, self.player.position.y + offSetY, 20, 200))


        #Update explosions
        for explosion in self.explosions:
            explosion.update()
            if explosion.intensity == 0:
                self.explosions.remove(explosion)


    def draw(self, screen):
        screen.fill((0, 0, 0))

        for asteroid in self.asteroids:
            asteroid.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

        for explosion in self.explosions:
            explosion.draw(screen)

        if not self.gameOver:
            self.player.draw(screen)

        screen.blit(self.scoreTextSurface, self.scoreTextRect)

        if self.win:
            screen.blit(self.winTextSurface, self.winTextRect)

        if self.gameOver:
           screen.blit(self.gameOverTextSurface, self.gameOvertextRect)

        pygame.display.update()



    def shoot(self):
        offSetX = math.cos(self.player.angle) * self.player.radius
        offSetY = math.sin(self.player.angle) * self.player.radius
        self.bullets.append(Bullet(self.player.position.x + offSetX, self.player.position.y + offSetY, self.player.angle))

    def spawnAsteroids(self, screen):
        self.asteroids.clear()
        for i in range(self.numberOfAsteroids):
            self.asteroids.append(Asteroid(random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()), random.randrange(20, 80)))
            while circleCollision(self.asteroids[i].position.x, self.asteroids[i].position.y, self.asteroids[i].radius, self.player.position.x, self.player.position.y, self.player.radius + 250):
                self.asteroids.pop()
                self.asteroids.append(Asteroid(random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()), random.randrange(20, 80)))

    def renderScoreToSurface(self):
        self.scoreTextSurface = self.font1.render(("Score: %d" % (self.score)), True, (255, 255, 255))

    def restart(self, screen):
        self.player.reset(screen.get_width() / 2, screen.get_height() / 2)
        self.spawnAsteroids(screen)
        self.bullets.clear()
        self.explosions.clear()
        self.score = 0
        self.renderScoreToSurface()
        self.win = False
        self.gameOver = False
        self.gameOverTimer = 0