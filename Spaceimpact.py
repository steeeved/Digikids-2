import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
window = pygame.display.set_caption("Ben Wainaina")
done = True
while done == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            done = False
    pygame.display.flip()