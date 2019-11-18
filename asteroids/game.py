import pygame
import random

from asteroid import *
from player import *
from collision import *
from gameState import *


class Game:

    def __init__(self, widht, height, title):
        #Init pygame
        pygame.init()

        # Create screen
        self.screen = pygame.display.set_mode((widht, height), pygame.FULLSCREEN | pygame.HWSURFACE)

        # Set title
        pygame.display.set_caption(title)

        #Create gameState
        self.gameState = GameState(self.screen)

        #Enter game loop
        self.run()


    def run(self):

        #fps is 120
        dt = 1 / 120

        newTime = 0
        frameTime = 0

        currentTime = pygame.time.get_ticks()

        accumulator = dt

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


            newTime = pygame.time.get_ticks()

            # deltaTime in seconds.
            frameTime = (newTime - currentTime) / 1000.0

            currentTime = newTime

            if frameTime > 0.15:
                frameTime = 0.15

            accumulator += frameTime

            while accumulator >= dt:
                self.gameState.handleInput(self.screen)
                self.gameState.update(self.screen)

                accumulator -= dt

            self.gameState.draw(self.screen)