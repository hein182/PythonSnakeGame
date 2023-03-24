import pygame
import random


GAME_WIDTH = 1280
GAME_HEIGHT = 720

arrX = []
#all possible positions by 20 on xy so it can collide with snake
for i in range(0, GAME_WIDTH, 20):
    arrX.append(i)
arrY = []
for i in range(0, GAME_HEIGHT, 20):
    arrY.append(i)

    #q: size of arrY =
    #a: 54
    #q: size of arrX =
    #a: 96


class Fruit:
    score = 0
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

    def checks_collision(self, snake):
        if snake.x == self.x and snake.y == self.y:
            snake.grow()
            self.x = arrX[random.randint(0, len(arrX)-1)]
            self.y = arrY[random.randint(0, len(arrY)-1)]
            Fruit.score += 1




    
        
    