import pygame

pygame.init()
window = pygame.display.set_mode((300, 200))
window = pygame.display.set_caption("My first pygame program")
done = True
while done == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            done = False
    pygame.display.flip()
