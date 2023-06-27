import pygame
from pygame.locals import *
from main import *

pygame.init()

screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)

rock = pygame.transform.scale(pygame.image.load('rock.png'), (42, 42))
paper = pygame.transform.scale(pygame.image.load('paper.png'), (32, 32))
scissors = pygame.transform.scale(pygame.image.load('scissors.png'), (40, 40))

inds = ()
inds += tuple([Individual(1) for _ in range(100)])
inds += tuple([Individual(2) for _ in range(100)])
inds += tuple([Individual(3) for _ in range(1000)])

fps = 25
clock = pygame.time.Clock()
while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 1
            if event.key == K_DOWN:
                fps -= 1
        if event.type == QUIT:
            pygame.quit()

    for i in range(len(inds)):
        for c in range(i+1, len(inds)):
            if collison(inds[i], inds[c]):
                inds[i].direction = choice((-1, 1)), choice((-1, 1))
                inds[c].direction = choice((-1, 1)), choice((-1, 1))

                if inds[i].type != inds[c].type:
                    possibilities = [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)]
                    results = [2, 2, 1, 1, 3, 3]
                    new_type = results[possibilities.index((inds[i].type, inds[c].type))]
                    inds[i].type, inds[c].type = new_type, new_type

    for ind in inds:
        ind.move()
        if ind.type == 1:
            screen.blit(rock, ind.pos)
        if ind.type == 2:
            screen.blit(paper, ind.pos)
        if ind.type == 3:
            screen.blit(scissors, ind.pos)

    pygame.display.update()

