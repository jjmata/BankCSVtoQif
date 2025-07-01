import math
import random
import sys

import pygame

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors for different slimes
def random_color():
    return (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255),
    )

class Slime:
    def __init__(self, position, radius=40):
        self.pos = list(position)
        self.radius = radius
        self.color = random_color()
        self.dragging = False
        self.offset = (0, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if math.hypot(event.pos[0] - self.pos[0], event.pos[1] - self.pos[1]) < self.radius:
                self.dragging = True
                self.offset = (self.pos[0] - event.pos[0], self.pos[1] - event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.pos = [event.pos[0] + self.offset[0], event.pos[1] + self.offset[1]]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ASMR Slime")
    clock = pygame.time.Clock()

    slimes = [Slime((random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))) for _ in range(3)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    slimes.append(Slime((random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))))
            for slime in slimes:
                slime.handle_event(event)

        screen.fill((30, 30, 40))
        for slime in slimes:
            slime.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
