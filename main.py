import sys
#include pygame
import pygame
import keyboard
#include snake.py
import snake
import fruit
import score

#constants
GAME_WIDTH = 1280
GAME_HEIGHT = 720
fps = 20
snake_size = 20
snake_speed = 20
snake_color = (0, 255, 0)
snake_start_x = 100
snake_start_y = 100

fruit_color = (255, 0, 0)

# Initialize pygame
pygame.init()

#clock
clock = pygame.time.Clock()

# Set the window size
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#fit screen to window
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# Set the window title
pygame.display.set_caption("Snake")

#create snake
snake1 = snake.Snake(snake_start_x, snake_start_y, "right", snake_color, snake_size)
fruit1 = fruit.Fruit(400, 300, fruit_color, snake_size)
score1 = score.Score(10, 10, (255, 255, 255), 30)

def main():
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            #check for collisons
            if snake1.check_collision():
                while True:
                    score1.gameOver(window)
                    score1.restart(window)
                    pygame.display.update()
                    if keyboard.is_pressed("r"):
                        #reset game
                        # snake1 = snake.Snake(snake_start_x, snake_start_y, "right", snake_color, snake_size)
                        snake1.x = snake_start_x
                        snake1.y = snake_start_y
                        snake1.direction = "right"
                        snake1.body = []
                        snake1.body.append((snake1.x, snake1.y))
                        # fruit = fruit.Fruit(400, 300, fruit_color, snake_size)
                        fruit1.x = 400
                        fruit1.y = 300
                        # score1 = score.Score(10, 10, (255, 255, 255), 30)
                        score1.score = 0
                        fruit.Fruit.score = 0
                        break
                    elif keyboard.is_pressed("escape"):
                        #minimize window
                        pygame.display.iconify()
                        #pause game
                        while True:
                            if keyboard.is_pressed("escape"):
                                break
                            else:
                                continue
            #check for key presses
            if keyboard.is_pressed("up"):
                if snake1.direction == "down":
                    continue
                snake1.change_direction("up")
            elif keyboard.is_pressed("down"):
                if snake1.direction == "up":
                    continue
                snake1.change_direction("down")
            elif keyboard.is_pressed("left"):
                if snake1.direction == "right":
                    continue
                snake1.change_direction("left")
            elif keyboard.is_pressed("right"):
                if snake1.direction == "left":
                    continue
                snake1.change_direction("right")
            elif keyboard.is_pressed("escape"):
                #minimize window
                pygame.display.iconify()
                #pause game
                while True:
                    if keyboard.is_pressed("escape"):
                        break
                    else:
                        continue



        window.fill((0, 70, 20))
        # draw here

        

        fruit1.draw(window)
        fruit1.checks_collision(snake1)

        snake1.draw(window)
        snake1.move(snake_speed)
        snake1.check_collision()

        score1.draw(window)

        #make game run smoothly

        pygame.display.update()

if __name__ == "__main__":
    main()