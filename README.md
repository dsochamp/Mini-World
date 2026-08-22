# Mini World Generator

<img src='Image.png' style='border-radius:25px; corner-shape:squircle;'>


This mini world generator uses Perlin noise to generate randomly generated worlds. There are three world types, lava, regular and random which randomly generates colours. 

## How to install

Open <a href='https://dsochamp.github.io/Mini-World'>dsochamp.github.io/Mini-World</a> and download the executable. This will be downloaded as a ```.zip``` file, unzip the zip file and navigate to the Dist folder and double click main. The executable may not work on Windows.

## How it works

The Mini World Generator uses a Python library called noise to generate perlin noise from a seed. This noise initially produces a grayscale image.  We then use the grayscale values, representing the darkness of each pixel, to create elevation and associate it with colours.  In regular mode, the lowest elevation is the ocean, which is blue, while the highest is snow atop the mountains, which is white. A nested for loop assigns these colours to each pixel.

To generate boats, I used ```random.randint(1, 500)``` when the elevation falls within the ocean threshold.  If the number is 1, a boat is spawned, creating a 1/500 chance of spawning.  Since the loops iterate from left to right across each row, when a boat is created, ```boatadd``` is set to ```True``` and the pixel count increments by 1.  While ```boatadd``` is ```True```, the ocean colour is set to brown. After 10 iterations (adding 1 to the pixel count of the boat 10 times), the loop resets and the ocean colour reverts to blue (in regular mode).

Sheep generate similarly but at a lower rate. This coding ensures that boat colour and sheep colour is only applied to ocean elevations and not to other elevations.

### Python Libraries

- PIL (Python Image Library)
- Noise
- Random

## Why I made it

I made this project out of curiosity when I watched a YouTube video on how Minecraft works. I found a Medium article on how to use perlin noise inside python. Perlin noise generates randomness but with smooth transitions which makes it perfect to simulate world terrain generation which I found very fascinating.
