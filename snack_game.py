import pygame
import random


def init_game():
    pygame.init()
    width, height = 600, 400
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    return win, width, height


def draw_snake(win, snake, size):
    for i, segment in enumerate(snake):
        color = (0, 200, 0) if i == 0 else (0, 255, 0)
        pygame.draw.rect(win, color, (segment[0], segment[1], size, size), border_radius=5)


def main():
    win, width, height = init_game()
    clock = pygame.time.Clock()
    snake_size = 20
    snake = [[width // 2, height // 2]]
    direction = "RIGHT"
    food = [random.randrange(0, width, snake_size), random.randrange(0, height, snake_size)]
    running = True

    while running:
        win.fill((30, 30, 30))
        pygame.draw.rect(win, (255, 0, 0), (food[0], food[1], snake_size, snake_size), border_radius=5)
        draw_snake(win, snake, snake_size)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        head = list(snake[0])
        if direction == "UP":
            head[1] -= snake_size
        elif direction == "DOWN":
            head[1] += snake_size
        elif direction == "LEFT":
            head[0] -= snake_size
        elif direction == "RIGHT":
            head[0] += snake_size

        if head in snake or head[0] < 0 or head[1] < 0 or head[0] >= width or head[1] >= height:
            running = False
            break

        snake.insert(0, head)
        if head == food:
            food = [random.randrange(0, width, snake_size), random.randrange(0, height, snake_size)]
        else:
            snake.pop()

        clock.tick(6)

    pygame.quit()
    print(f"Game Over! Final Score: {len(snake) - 1}")


if __name__ == "__main__":
    main()
