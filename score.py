import fruit
import pygame

fruit.Fruit.score = 0
GAME_WIDTH = 1280
GAME_HEIGHT = 720

class Score:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw(self, window):
        font = pygame.font.SysFont("comicsans", 30, True)
        text = font.render("Score: " + str(fruit.Fruit.score), 1, self.color)
        window.blit(text, (self.x, self.y))

    def gameOver(self, window):
        font = pygame.font.SysFont("comicsans", 30, True)
        text = font.render("Game Over", 1, self.color)
        window.blit(text, (GAME_WIDTH/2 - 50, GAME_HEIGHT/2 - 30))

    def restart(self, window):
        font = pygame.font.SysFont("comicsans", 30, True)
        text = font.render("Press 'r' to restart", 1, self.color)
        window.blit(text, (GAME_WIDTH/2 - 80, GAME_HEIGHT/2 + 30))