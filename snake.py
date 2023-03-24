import pygame

GAME_WIDTH = 1280
GAME_HEIGHT = 720

class Snake:
    def __init__(self, x, y, direction, color, size):
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.color = color
        self.body = []
        self.body.append((self.x, self.y))

    def move(self, speed):
        if self.direction == "up":
            self.y -= 1 * speed
        elif self.direction == "down":
            self.y += 1 * speed
        elif self.direction == "left":
            self.x -= 1 * speed
        elif self.direction == "right":
            self.x += 1 * speed
        self.body.append((self.x, self.y))
        self.body.pop(0)

    def draw(self, window):
        for x, y in self.body:
            if(x == self.x and y == self.y):
                pygame.draw.rect(window, self.color, (x, y, self.size, self.size))
            #elif the body is even index
            elif(self.body.index((x, y)) % 2 == 0):
                pygame.draw.rect(window, (123, 69, 70), (x, y, self.size, self.size))
            else:
                pygame.draw.rect(window, (0, 0, 255), (x, y, self.size, self.size))

    def change_direction(self, direction):
        self.direction = direction
    
    def grow(self):
        match(self.direction):
            case "up":
                self.body.append((self.x, self.y + 40))
            case "down":
                self.body.append((self.x, self.y - 40))
            case "left":
                self.body.append((self.x + 40, self.y))
            case "right":
                self.body.append((self.x - 40, self.y))


    def check_collision(self):
        #if body goes out of board bring to opposite side
        if self.x > GAME_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = GAME_WIDTH
        elif self.y > GAME_HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = GAME_HEIGHT
        #print out the values of the body and snake head
        for x, y in self.body:
            #dont count collision with neweest body part
            if self.body.index((x, y)) != len(self.body) - 1:
                if self.x == x and self.y == y:
                    print("collision")
                    return True
                    
        #   print(x, y) 
        
        print(self.x, self.y)
        return False
    