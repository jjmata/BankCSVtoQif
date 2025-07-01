import math
import random
import pygame

# Simple Coin Slicer game using Pygame
# Coins appear from the bottom and move upward.
# Slice them with the mouse to score points.

# Constants
WIDTH, HEIGHT = 800, 600
COIN_RADIUS = 20
COIN_COLOR = (255, 215, 0)  # Gold
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

class Coin:
    def __init__(self):
        self.x = random.randint(COIN_RADIUS, WIDTH - COIN_RADIUS)
        self.y = HEIGHT + COIN_RADIUS
        self.speed_y = random.uniform(-15, -8)
        self.sliced = False

    def update(self):
        self.y += self.speed_y
        self.speed_y += 0.5  # gravity
        if self.y > HEIGHT + COIN_RADIUS:
            self.sliced = True

    def draw(self, screen):
        pygame.draw.circle(screen, COIN_COLOR, (int(self.x), int(self.y)), COIN_RADIUS)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    coins = []
    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                mx, my = event.pos
                for coin in coins:
                    if not coin.sliced and math.hypot(mx - coin.x, my - coin.y) <= COIN_RADIUS:
                        coin.sliced = True
                        score += 1

        if random.random() < 0.02:
            coins.append(Coin())

        screen.fill(BACKGROUND_COLOR)
        for coin in coins:
            coin.update()
            if not coin.sliced:
                coin.draw(screen)
        coins = [c for c in coins if not c.sliced]

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    print("Final Score:", score)

if __name__ == "__main__":
    main()
