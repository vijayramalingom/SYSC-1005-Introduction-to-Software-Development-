import sys

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

def weighted_grayscale(image):
    """ (Cimpl.Image) -> None
    
    Refactored version of grayscale function which takes into account how the 
    human eye preceives brigtness. Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> weighted_grayscale(image)
    >>> show(image)    
    """    
    for  x, y, (r, g, b) in image:
        brightness = (r * 0.299) + (g * 0.587) + (b * 0.114)
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)
 
def negative(image):
    """ (Cimpl.Image) -> None
    
    Convert image into opposite colour.
    
    >>> image = load_image(choose_file()) 
    >>> negative(image)
    >>> show(image)    
    """    
    for  x, y, (r, g, b) in image:
        neg = create_color(255 - r, 255 - g, 255 - b)
        set_color(image, x, y, neg)

def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    
    Modify image, maximizing the contrast between light and dark pixels.
    
    >>> image = load_image(choose_file()) 
    >>> extreme_contrast(image)
    >>> show(image)    
    """      
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
    """ (Cimpl.Image) -> None
    
    Convert image into sepia tones
    
    >>> image = load_image(choose_file()) 
    >>> sepia_tint(image)
    >>> show(image)    
    """      
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
    """ (int) -> int
    
    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.
    
    >>>  _adjust_component(10)
    31
    _adjust_component(85)
    95
    _adjust_component(142)
    159
    _adjust_component(230)
    223
    """      
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
    """ (Cimpl.Image) -> None
    
   "Posterize" the specified image.
    
    >>> image = load_image(choose_file()) 
    >>> posterize(image)
    >>> show(image)    
    """          
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
    """ (Cimpl.Image, float) -> None
    
    Modify Image using Edge Detection
    
    >>> image = load_image(choose_file()) 
    >>> detect_edges(image, 10)
    >>> show(image)    
    """          
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
    """ (Cimpl.Image, float) -> None
    
    Modify Image using Edge Detection
    
    >>> image = load_image(choose_file()) 
    >>> detect_edges_better(image, 10)
    >>> show(image)    
    """              
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

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

if __name__ == "__main__":
    done = False
    img = 1
    while not done:
        command = input("Enter a command: L for load image, N for negative, G for grayscale, X for extreme contrast, S for sepia tint, E for detect edges and Q to quit the program")
        if command == 'L':
            img = get_image()
            show(img)
        elif command == 'N':
            if img == 1:
                print("no image loaded")
            else:
                negative(img)
                show(img)
        elif command == 'G':
            if img == 1:
                print("no image loaded")
            else:
                grayscale(img)
                show(img)
        elif command == 'X':
            if img == 1:
                print("no image loaded") 
            else:
                extreme_contrast(img)
                show(img) 
        elif command == 'S':
            if img == 1:
                print("no image loaded")
            else:
                sepia_tint(img)
                show(img) 
        elif command == 'E':
            if img == 1:
                print("no image loaded")
            else:
                threshold = int(input("enter a threshold"))
                detect_edges_better(img,threshold)
                show(img)        
        elif command == 'Q':
            print("You have quit the program")
            done = True
        else:
            print("No such Command")
    
        
    
    
