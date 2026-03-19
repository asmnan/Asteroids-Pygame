from logger import log_state
import pygame
#from module_name import my_function
from constants import *
def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}\n Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill("black")
        pygame.display.flip()
if __name__ == "__main__":
    main()
