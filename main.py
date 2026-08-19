import noise
import numpy as np
from PIL import Image
import random

worldtype = input('Would you like "lava" or "regular"? (Type anything else for random colours)  ')
worldsize = int(input('How big would you like your world (in px)?'))

shape = (worldsize, worldsize)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)

if worldtype == 'regular':
    ocean = [65,105,225]
    mainland = [34,139,34]
    shore = [238, 214, 175]
    top = [255, 250, 250]
    mountain = [139, 137, 137]
elif worldtype == 'lava':
    ocean = [224, 104, 10]
    mainland = [128, 0, 0]
    shore = [238, 214, 175]
    top = [228, 34, 23]
    mountain = [85,0,0]
else:
    ocean = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    mainland = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    shore = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    top = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    mountain = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]



def add_color(world):
    boatadd = 0
    addsheep = 0

    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.05:
                if random.randint(0, 5000) == 1 and boatadd == 0:
                    color_world[i][j] = [205, 127, 50]
                    boatadd = 1
                elif 0 < boatadd < 5:
                    color_world[i][j] = [205, 127, 50]
                    boatadd += 1
                elif 5 <= boatadd < 10:
                    color_world[i][j] = [180, 100, 42]
                    boatadd += 1
                elif boatadd == 10:
                    color_world[i][j] = [205, 127, 50]
                    boatadd = 0
                else:
                    color_world[i][j] = ocean
            elif world[i][j] < 0:
                color_world[i][j] = shore
            elif world[i][j] < 0.05:
                if worldtype == 'lava':
                    color_world[i][j] = [random.randint(128,210), random.randint(0, 105), random.randint(0,45)]
                elif worldtype == 'regular':
                    color_world[i][j] = [random.randint(35,145), random.randint(100,205), random.randint(34,152)]
                else:
                    color_world[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
            elif world[i][j] < 0.25:
                if random.randint(0,1000) == 1 and addsheep == 0:
                    color_world[i][j] = [255,255,255]
                    addsheep += 1
                elif addsheep == 1:
                    color_world[i][j] = [201,201,201]
                    addsheep = 0
                else:
                    color_world[i][j] = mainland
            elif world[i][j] < 0.3:
                color_world[i][j] = mountain
            elif world[i][j] < 1.0:
                color_world[i][j] = top

    return color_world

color_world = add_color(world)
Image.fromarray((color_world).astype(np.uint8)).show()