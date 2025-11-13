import pygame
import random 


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png").convert_alpha()
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")

        mole_x, mole_y = 0, 0
        
        clock = pygame.time.Clock()
        running = True

        def grid():
            color = (0,0,0)
            for x in range(640, 32):
                pygame.draw.line(screen, color, (x,0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, color, (0,y), (640,y))
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = mole_image.get_rect(topleft = (mole_x, mole_y))

                if mole_rect.collidepoint(mouse_x,mouse_y): 
                    mole_x = random.randrange(0, 640) * 32
                    moly_y = random.randrange(0, 512) * 32

                screen.fill((144,238,144))
                grid()
                screen.bilt(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

                pygame.display.flip()
                clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
