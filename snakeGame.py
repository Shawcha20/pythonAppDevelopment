import pygame
import random

# initialize pygame
pygame.init()

# screen dimension
WIDTH, HEIGHT = 800, 700

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# game variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
foodPos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
foodSpawn = True
direction = 'RIGHT'
changeTo = direction
score = 0

def gameOver():
    pygame.quit()
    quit()

clock = pygame.time.Clock()

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                changeTo = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                changeTo = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                changeTo = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                changeTo = "RIGHT"

    # update direction
    if changeTo == "UP":
        direction = "UP"
    elif changeTo == "DOWN":
        direction = "DOWN"
    elif changeTo == "LEFT":
        direction = "LEFT"
    elif changeTo == "RIGHT":
        direction = "RIGHT"

    # update snake position
    if direction == "UP":
        snakePos[1] -= 10
    elif direction == "DOWN":
        snakePos[1] += 10
    elif direction == "LEFT":
        snakePos[0] -= 10
    elif direction == "RIGHT":
        snakePos[0] += 10

    # snake body growth
    snakeBody.insert(0, list(snakePos))
    if snakePos == foodPos:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    if not foodSpawn:
        foodPos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    foodSpawn = True

    # collision with wall
    if snakePos[0] < 0 or snakePos[0] >= WIDTH:
        gameOver()
    if snakePos[1] < 0 or snakePos[1] >= HEIGHT:
        gameOver()

    # collision with itself
    for block in snakeBody[1:]:
        if snakePos == block:
            gameOver()

    # draw
    screen.fill(BLACK)
    for pos in snakeBody:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # update display
    pygame.display.update()
    clock.tick(15)
