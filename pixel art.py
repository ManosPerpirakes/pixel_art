import pygame
pygame.init()
from random import randint

rectangles = []
colours = []
w = pygame.display.set_mode((1500, 750))
x = 0
y = 0
for i in range(1250):
    colours.append((randint(0, 255), randint(0, 255), randint(0, 255))) 
for i in range(25):
    for i in range(50):
        rectangles.append(pygame.Rect(x, y, 30, 30))
        x += 30
    x = 0
    y += 30
close = False
clock = pygame.time.Clock()
while close != True:
    w.fill((255, 255, 255))
    for i in range(1250):
        pygame.draw.rect(w, colours[i], rectangles[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
    pygame.display.update()
    clock.tick(60)