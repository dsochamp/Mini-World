import noise
import numpy as np
from PIL import Image
import random

shape = (1024,1024)
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

blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]



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
                    color_world[i][j] = blue
            elif world[i][j] < 0:
                color_world[i][j] = beach
            elif world[i][j] < 0.05:
                color_world[i][j] = [random.randint(164,234), random.randint(160,221), random.randint(42,101)]
            elif world[i][j] < 0.25:
                if random.randint(0,1000) == 1 and addsheep == 0:
                    color_world[i][j] = [255,255,255]
                    addsheep += 1
                elif addsheep == 1:
                    color_world[i][j] = [201,201,201]
                    addsheep = 0
                else:
                    color_world[i][j] = green
            elif world[i][j] < 0.3:
                color_world[i][j] = mountain
            elif world[i][j] < 1.0:
                color_world[i][j] = snow

    return color_world

color_world = add_color(world)
Image.fromarray((color_world).astype(np.uint8)).show()