from Cimpl import *
import random

#Exercise 1

#makes img red
def red_channel(image):
    for x, y, (r, g, b) in image:
        new_color = create_color(r, 0, 0)
        set_color(image, x, y, new_color)
    show(image)

#makes img green
def green_channel(image):
    for x, y, (r, g, b) in image:
        new_color = create_color(0, g, 0)
        set_color(image, x, y, new_color)
    show(image)

#makes img blue
def blue_channel(image):
    for x, y, (r, g, b) in image:
        new_color = create_color(0, 0, b)
        set_color(image, x, y, new_color)
    show(image)

#Exercise 2

def reduce_brightness(image, multiplier):
    for x, y, (r, g, b) in image:
        new_color = create_color(r * multiplier, g * multiplier, b * multiplier)
        set_color(image, x, y, new_color)
    show(image)    

#Exercise 3

def swap_red_blue(image):
    for x, y, (r, g, b) in image:
        new_color = create_color(b, g, r)
        set_color(image, x, y, new_color)
    show(image)

#Exercise 4

def hide_image(image):
    for x, y, (r, g, b) in image:
        avg = ((r + g + b) / 3) // 10
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_color = create_color(avg, g, b)
        set_color(image, x, y, new_color)
    show(image)
    
def recover_image(image):
    for x, y, (r, g, b) in image:
        new_color = create_color(r*10, 128, 128)
        set_color(image, x, y, new_color)
    show(image)    

    
image = load_image(choose_file())

reduce_brightness(image, 0.25)

        
