import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([0, 0, 255])
pygame.draw.circle(screen, [0,255,0], [380,55], 50, 0)
pygame.draw.rect(screen, [255,0,0], [5,5,300,200], 0)
pygame.display.flip()
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

