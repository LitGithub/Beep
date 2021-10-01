import pygame
import winsound
import random
pygame.init()
display = pygame.display.set_mode((1000, 1000))
for x in range(10):
    pygame.draw.rect(display, (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)), (100 * x, 0, 100, 1000))
pygame.display.flip()

toggled = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sounds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
currentRectangle = -1
mousePos = [0, 0]

for k in range(10):
    sounds[k] = ((32767 - 37) / 9) * (k) + 37


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        toggled[currentRectangle] = True

    if event.type == pygame.MOUSEBUTTONUP:
        toggled[currentRectangle] = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

    for i in range(10):
        if mousePos[0] >= 100 * i and mousePos[0] <= 100 * i + 100:
            currentRectangle = i
        if toggled[i] == True:
            print("In rect: ", i, " Sound: ", sounds[i])
            winsound.Beep(int(sounds[i]),500)
            toggled[i] = False

pygame.quit()

#import winsound
#import math
#import random
#for x in range(10000):
#    print(int(1000 * math.sin(x) +(1037)))
#    winsound.Beep(int(10000 * math.sin(random.randrange(0, 1000000)) +(10037)), random.randrange(10, 1000))
#    #37 thru 32767
