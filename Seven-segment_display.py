import pygame
from datetime import datetime

pygame.init()

# SCREEN SETUP
WIDTH, HEIGHT = 730, 200
root = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = "Seven-segment display"
pygame.display.set_caption(TITLE)
FPS = 30

# COLORS
MAIN_COLOR = (0, 0, 0)
SECUNDARY_COLOR = (15, 15, 15)
TEXT_COLOR = (237, 218, 109)

# NUMBERS BIN
abcdefg = [
    "1111110",
    "0110000",
    "1101101",
    "1111001",
    "0110011",
    "1011011",
    "1011111",
    "1110000",
    "1111111",
    "1111011",
]

# CLASSES
class Digit:
    def __init__(self, screen, posX, posY, offcolor, oncolor):
        self.screen = screen
        self.posX = posX
        self.posY = posY
        self.offcolor = offcolor
        self.oncolor = oncolor
        self.rects = [
            (self.posX + 20, self.posY, 60, 20),  # A
            (self.posX + 80, self.posY + 20, 20, 60),  # B
            (self.posX + 80, self.posY + 100, 20, 60),  # C
            (self.posX + 20, self.posY + 160, 60, 20),  # D
            (self.posX, self.posY + 100, 20, 60),  # E
            (self.posX, self.posY + 20, 20, 60),  # F
            (self.posX + 20, self.posY + 80, 60, 20),  # G
        ]

    def draw(self, color, coords):
        pygame.draw.rect(self.screen, color, coords, border_radius=5)

    def glow(self, bin):
        for i, j in enumerate(bin):
            if j == "1":
                self.draw(self.oncolor, self.rects[i])
            else:
                self.draw(self.offcolor, self.rects[i])


# OBJECTS
digital_clock = [
    Digit(root, 10, 10, SECUNDARY_COLOR, TEXT_COLOR),
    Digit(root, 120, 10, SECUNDARY_COLOR, TEXT_COLOR),
    Digit(root, 260, 10, SECUNDARY_COLOR, TEXT_COLOR),
    Digit(root, 370, 10, SECUNDARY_COLOR, TEXT_COLOR),
    Digit(root, 510, 10, SECUNDARY_COLOR, TEXT_COLOR),
    Digit(root, 620, 10, SECUNDARY_COLOR, TEXT_COLOR),
]


def draw():
    root.fill(MAIN_COLOR)
    dt_string = datetime.now().strftime("%H%M%S")
    for i, j in enumerate(dt_string):
        digital_clock[i].glow(abcdefg[int(j)])

    # LEFT SEPARATOR
    pygame.draw.rect(
        root,
        TEXT_COLOR,
        (230, HEIGHT - (HEIGHT // 3 * 2) - 20, 20, 20),
        border_radius=5,
    )
    pygame.draw.rect(
        root, TEXT_COLOR, (230, HEIGHT - HEIGHT // 3 - 5, 20, 20), border_radius=5
    )

    # RIGHT SEPARATOR
    pygame.draw.rect(
        root,
        TEXT_COLOR,
        (480, HEIGHT - (HEIGHT // 3 * 2) - 20, 20, 20),
        border_radius=5,
    )
    pygame.draw.rect(
        root, TEXT_COLOR, (480, HEIGHT - HEIGHT // 3 - 5, 20, 20), border_radius=5
    )
    pygame.display.update()


# MAIN LOOP
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        draw()


main()
