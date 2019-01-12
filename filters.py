""" SYSC 1005 A Fall 2017.

Filters for a photo-editing application.
"""

from Cimpl import *

def grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def solarize(image, threshold):
    """ (Cimpl.Image) -> None
    
    Solarize image.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image)     
    """
    for x, y, (red, green, blue) in image:

        # Invert the values of all RGB components that are less than 128,
        # leaving components with higher values unchanged.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        solarized = create_color(red, green, blue)
        set_color(image, x, y, solarized)


def black_and_white(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3      
        
        if brightness < 128:
            set_color(image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(image, x, y, white)


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white-and-gray (three-tone) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:      
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)

#Exercise 2

def weighted_grayscale(image):
    for  x, y, (r, g, b) in image:
        brightness = (r * 0.299) + (g * 0.587) + (b * 0.114)
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)
 
 #Exercise 3
 
def negative(image):
    for  x, y, (r, g, b) in image:
        neg = create_color(255 - r, 255 - g, 255 - b)
        set_color(image, x, y, neg)


def extreme_contrast(image):
    for  x, y, (r, g, b) in image:
        if r < 128:
            r = 0
        else:
            r = 255
        if b < 128:
            b = 0
        else:
            b = 255
        if g < 128:
            g = 0
        else:
            g = 255
        
        cont = create_color(r, g, b)
            
        set_color(image, x, y, cont)
        
def sepia_tint(image):
    grayscale(image)
    for x, y, (red, green, blue) in image:  
        if red < 63:
            tint = create_color(red*1.1,green,blue*0.9)
        elif red < 191:
            tint = create_color(red*1.15,green, blue*0.85)
        else:                  
            tint = create_color(red*1.08, green, blue*0.93)
        set_color(image, x, y, tint)

def _adjust_component(amount):
    if amount < 64:
        amount = 31
    elif amount < 128:
        amount = 95
    elif amount < 192:
        amount = 159
    else:
        amount = 223
    
    return amount

def posterize(img):
    for x, y, (red, green, blue) in image:
        post = create_color(_adjust_component(red), green, blue)
        set_color(image, x, y, post)

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

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red ) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green ) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue ) // 5

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target