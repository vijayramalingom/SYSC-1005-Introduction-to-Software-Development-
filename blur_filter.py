# SYSC 1005 Fall 2017

from Cimpl import *

def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(source)):
    #     for x in range(0, get_width(source)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)
            topleft_red, topleft_green, topleft_blue = get_color(source, x-1, y-1)
            topright_red, topright_green, topright_blue = get_color(source, x+1, y-1)
            bottomleft_red, bottomleft_green, bottomleft_blue = get_color(source, x-1, y+1)
            bottomright_red, bottomright_green, bottomright_blue = get_color(source, x+1, y+1)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + topleft_red + topright_red + bottomleft_red + bottomright_red ) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green +  topright_green + bottomleft_green + bottomright_green ) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue + topright_blue + bottomleft_blue + bottomright_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def test_blur():
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)
    
    
def make_very_blurry(number_of_blurs):
    image = load_image(choose_file())
    
    for i in range(number_of_blurs):
        image = blur(image)  # Blur the image repeatedly

    show(image)  
    

# Exercise: This filter doesn't blur the pixels along the image's edges.
# Here is one way we could extend the filter to do this:
#
# Visit the four corner pixels, blurring each one by averaging the pixel's
# components with those of its two neightbours; e.g., blur the pixel
# @ (0, 0) by using the components @ (0, 0), (1, 0) and (0, 1).
#
# Next, visit all the pixels on the edges except for the corner pixels.
# Blur each pixel by averaging the pixel's components with those of its
# three neigbours; e.g., blur the pixel @ (1, 0) by using the components
# @ (1, 0), (0, 0), (1, 1) and (2, 0).
#
# Make this change to the filter.

def detect_edges(image, threshold):
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image)):
            r1,g1,b1 = get_color(image, x, y)
            r2,g2,b2 = get_color(image, x, y + 1)
            avg1 = (r1 + g1 + b1) / 3
            avg2 = (r2 + g2 + b2) / 3
            difference = abs(avg1 - avg2)
            if (difference > threshold):
                set_color(image, x, y, black)
            elif (difference < threshold):
                set_color(image, x, y, white)
                
def detect_edges_better(image, threshold):
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image) - 1):
            r1,g1,b1 = get_color(image, x, y)
            r2,g2,b2 = get_color(image, x, y + 1)
            rr,gr,br = get_color(image, x + 1, y)
            avg1 = (r1 + g1 + b1) / 3
            avg2 = (r2 + g2 + b2) / 3
            avgr = (rr + gr + br) / 3
            difference = abs(avg1 - avg2)
            differencer = abs(avg1 - avgr)
            if (difference > threshold) or (differencer > threshold):
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)

image = load_image(choose_file())

detect_edges_better(image,10)

show(image)

