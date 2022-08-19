# A visual representation of the Mandelbrot set
# The mandelbrot set refers to plotting of complex numbers used in an equation for 
# f(z) with an initial value of 0. The colors of the diagram are biased towards the 
# divergence of the iterations of the sequence at each given value of a, b.

# MODULES
import pygame
import math

RES = 1
# DATA DEFINITIONS
SCREEN = (800,800)
# Variables required by pygame
display = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
pygame.init()


colors = [[(0,0,0) for x in range(SCREEN[0])] for y in range(SCREEN[1])]

# DD. TILE
# tile = Tile()
# interp. an instance of the object tile
# attr.
# x position
# y position
# color

class Tile(pygame.sprite.Sprite):
    def __init__(self, x,y):
        self.x = x * RES
        self.y = y * RES
        self.color = (255,0,0)
        self.rect = pygame.Rect(self.x ,self.y, RES,RES)
        self.rect.topleft = self.x, self.y
    
    def drawRect(self,screen):
        pygame.draw.rect(screen,self.color, self.rect)

    

# DD. TILEROW
# tileRow = [TILE, ...]
# interp. a row of tiles
tileRow = []
for x in range(SCREEN[0]):
    newTile = Tile(x,0)

# DD. GRID
# grid = [TILEROW, ...]
# interp. a grid of tilerows
grid = []
for y in range(SCREEN[1]):
    tileRow = []
    for x in range(SCREEN[0]):
        newTile = Tile(x,y)
        tileRow.append(newTile)
    grid.append(tileRow)
# CODE

def draw():
    # display.fill("black")
    # for row in grid:
    #     for tile in row:
    #         tile.drawRect(display)
    for y in range(SCREEN[1]):
        for x in range(SCREEN[0]):
            display.set_at((x, y), colors[y][x])
            # display.fill(colors[y][x],(x,y,1,1))
    pygame.display.flip()

def remap(value, from1, to1, from2, to2):
    return (value - from1) / (to1 - from1) * (to2 - from2) + from2

unit = 1
ratio = 4
minX = -3
minY = -2
def update():
    global unit
    global minX
    global minY
    for y in range(SCREEN[1]):
        for x in range(SCREEN[0]):
            # The color of each tile is given by whether or not they are divergent during the iteration
            # Let n be the "counter" from the first iteration to divergence.
            n = 0
            # If n gets bigger than 16 during any of the iterations, then halt the process and map. This tile will be considered to diverge
            a = remap(x,0,SCREEN[0],-3,minX + ratio * unit)
            b = remap(y,0,SCREEN[1],-2,minY + ratio * unit)

            ca = a
            cb = b
            while n < 100:

                aa = a*a - b*b
                bb = 2 * a * b
                a = aa + ca
                b = bb + cb

                if abs(a+b) > 16:
                    break
                n+= 1
            # If the calculation makes it past n = 255, then color it white with a value of 255
            if n == 100:
                cl = 0
            else:
                cl = remap(n,0,100,0,255)
            colors[y][x] = (cl, cl, cl)

# def update():
#     for row in grid:
#         for tile in row:
#             # The color of each tile is given by whether or not they are divergent during the iteration
#             # Let n be the "counter" from the first iteration to divergence.
#             n = 0
#             # If n gets bigger than 16 during any of the iterations, then halt the process and map. This tile will be considered to diverge
#             a = remap(tile.x,0,SCREEN[0],-3,1)
#             b = remap(tile.y,0,SCREEN[1],-2,2)

#             ca = a
#             cb = b
#             while n < 100:

#                 aa = a*a - b*b
#                 bb = 2 * a * b
#                 a = aa + ca
#                 b = bb + cb

#                 if abs(a+b) > 16:
#                     break
#                 n+= 1
#             # If the calculation makes it past n = 255, then color it white with a value of 255
#             if n == 100:
#                 cl = 0
#             else:
#                 cl = remap(n,0,100,0,255)
#             tile.color = (cl, cl, cl)


def userInp():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

while True:
    draw()
    update()
    userInp()