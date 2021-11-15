import pygame


WIDTH, HEIGHT = 512, 512
WHITE = (255, 255, 255)

def main():
    while True:
        window.fill(WHITE)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")

