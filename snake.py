import sys
import pygame
import random

def main():
    size = width, height = 400, 300
    
    screen = pygame.display.set_mode(size)

    green_pix = pygame.image.load('snake_green.png')
    headrect = green_pix.get_rect()
    headrect.x, headrect.y = width // 2, height - 20

    foodrect = green_pix.get_rect()
    foodrect.x = random.randint(0, width // 10 - 1) * 10
    foodrect.y = random.randint(0, height // 10 - 1) * 10

    black_sq = pygame.image.load('blank_black.png')
    tailrect = black_sq.get_rect()

    screen.fill((0, 0, 0))

    direction = [0, -10]
    snakelength = 5
    segments = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = [10, 0]
                if event.key == pygame.K_LEFT:
                    direction = [-10, 0]
                if event.key == pygame.K_UP:
                    direction = [0, -10]
                if event.key == pygame.K_DOWN:
                    direction = [0, 10]

        segments.append((headrect.x, headrect.y))
        headrect.move_ip(direction)

        pygame.time.wait(100)

        if headrect.colliderect(foodrect):
            snakelength += 3
            foodrect.x = random.randint(0, width // 10 - 1) * 10
            foodrect.y = random.randint(0, height // 10 - 1) * 10
            

        while len(segments) > snakelength:
            tailrect.x, tailrect.y = segments.pop(0)
            screen.blit(black_sq, tailrect)

        screen.blit(green_pix, foodrect)
        screen.blit(green_pix, headrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
