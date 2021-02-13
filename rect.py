import pygame

pygame.init()

#window
win = pygame.display.set_mode((500, 500))
#name of the game
pygame.display.set_caption("My first program")
x = 100
y = 400
width = 40
height = 60
vel = 13

#game play
run = True
while run:
    pygame.time.delay(100)
    #checking for events that occur during the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #checking what keys have been pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    #filling game window with a color
    win.fill((0,0,0))
    #drawing objects in the game. Start with window(win), colour, coordinates, size
    pygame.draw.rect(win, (102, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()

        

