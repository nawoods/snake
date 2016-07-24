import sys
import pygame
import random

# lose the game
def lose():
    pass

def printSomething(message, color, xstart, ystart, screen):
    #list of pixels whose color was changed
    changed_pixels = []

    message = str(message)
    alphabet = {
        "0": [(0, 0), (10, 0), (20, 0), (0, 10), (20, 10), (0, 20), (20, 20),
        (0, 30), (20, 30), (0, 40), (10, 40), (20, 40)],
        "1": [(0, 0), (0, 10), (0, 20), (0, 30), (0, 40)],
        "2": [(0, 0), (10, 0), (20, 0), (20, 10), (0, 20), (10, 20), (20, 20),
        (0, 30), (0, 40), (10, 40), (20, 40)],
        "3": [(0, 0), (10, 0), (20, 0), (20, 10), (0, 20), (10, 20), (20, 20),
        (20, 30), (0, 40), (10, 40), (20, 40)],
        "4": [(0, 0), (20, 0), (0, 10), (20, 10), (0, 20), (10, 20), (20, 20),
        (20, 30), (20, 40)],
        "5": [(0, 0), (10, 0), (20, 0), (0, 10), (0, 20), (10, 20), (20, 20),
        (20, 30), (0, 40), (10, 40), (20, 40)],
        "6": [(0, 0), (10, 0), (20, 0), (0, 10), (0, 20), (10, 20), (20, 20),
        (0, 30), (20, 30), (0, 40), (10, 40), (20, 40)],
        "7": [(0, 0), (10, 0), (20, 0), (20, 10), (20, 20), (20, 30), (20,
        40)],
        "8": [(0, 0), (10, 0), (20, 0), (0, 10), (20, 10), (0, 20), (10, 20), 
        (20, 20), (0, 30), (20, 30), (0, 40), (10, 40), (20, 40)],
        "9": [(0, 0), (10, 0), (20, 0), (0, 10), (20, 10), (0, 20), (10, 20), 
        (20, 20), (20, 30), (0, 40), (10, 40), (20, 40)]
    }

    pix = pygame.image.load('snake_' + color + '.png')
    rect = pix.get_rect()

    for letter in message:
        for loc in alphabet[letter]:
            changed_pixels.append((xstart + loc[0], ystart + loc[1]))
            rect.x = xstart + loc[0]
            rect.y = ystart + loc[1]
            screen.blit(pix, rect)

        xstart += max([i[0] for i in alphabet[letter]]) + 20

    return changed_pixels

def game(width, height, screen):
    green_pix = pygame.image.load('snake_green.png')
    blue_pix = pygame.image.load('snake_blue.png')
    headrect = green_pix.get_rect()
    headrect.x, headrect.y = width // 2, height - 20

    foodrect = green_pix.get_rect()
    foodrect.x = random.randint(0, width // 10 - 1) * 10
    foodrect.y = random.randint(0, height // 10 - 1) * 10

    black_sq = pygame.image.load('blank_black.png')
    tailrect = black_sq.get_rect()

    screen.fill((0, 0, 0))

    score = 0
    score_pixels = []

    direction = [0, -10]
    snakelength = 5
    # coordinates of all current snake segments
    segments = []

    # flag variable to determine whether or not the game is on
    game_started = True

    while game_started:
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

        # milliseconds between snake movements
        pygame.time.wait(100)

        # what to do when food collected
        if headrect.colliderect(foodrect):
            snakelength += 3
            foodrect.x = random.randint(0, width // 10 - 1) * 10
            foodrect.y = random.randint(0, height // 10 - 1) * 10
            score += 1
            for i in score_pixels:
                tailrect.x, tailrect.y = i
                screen.blit(black_sq, tailrect)
            score_pixels = printSomething(score, "blue", 20, 20, screen)
            

        # get rid of extra tail segments
        while len(segments) > snakelength:
            tailrect.x, tailrect.y = segments.pop(0)
            if (tailrect.x, tailrect.y) in score_pixels:
                screen.blit(blue_pix, tailrect)
            else:
                screen.blit(black_sq, tailrect)

        # let the user see what's going on
        screen.blit(green_pix, foodrect)
        screen.blit(green_pix, headrect)
        pygame.display.flip()

        # if headrect is touching snake body, lose the game
        for i in segments:
            if (headrect.x, headrect.y) == i:
                game_started = False
                lose()

        # if headrect outside of screen, lose game
        if headrect.x < 0 or headrect.x >= width:
            game_started = False
            lose()
        if headrect.y < 0 or headrect.y >= height:
            game_started = False
            lose()

def main():
    size = width, height = 400, 300
    
    screen = pygame.display.set_mode(size)

    game(width, height, screen)


if __name__ == '__main__':
    main()
