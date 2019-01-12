""" SYSC 1005 A Fall 2017 Lab 4 Prelab
"""

from Cimpl import *

# maximize_red is used in Part 1, Exercise 1

def maximize_red(image):
   """ (Cimpl.Image) -> None
   
   Maximize the red component of every pixel in image,
   leaving the green and blue components unchanged.
   
   >>> image = load_image(choose_file()) 
   >>> maximize_red(image)
   >>> show(image)   
   """   
   # The for loop "visits" each pixel in image, row-by-row, starting with the
   # pixel in the upper-left corner and finishing with the pixel in the 
   # lower-right corner. For each pixel, we unpack its x and y coordinates
   # and its red, green and blue components, binding them to variables
   # x, y, r, g, and b, respectively. 
   
   # After a pixel's components are unpacked, the body of the for 
   # loop is executed. A new Color object is created, using the original
   # green and blue components, but with with the red component set to its
   # maximum value (255). The pixel's colour is changed to this new colour.
   # The for loop then visits the next pixel in the sequence, and the unpacking 
   # and modify-colour steps are repeated for that pixel.

   for x, y, (r, g, b) in image:
      new_color = create_color(255, g, b)
      set_color(image, x, y, new_color)
      
# reduce_red_50 is used in Part 1, Exercise 2      

def reduce_red_50(image):
   """  (Cimpl.Image) -> None
   
   Reduce the red component of every pixel in image to 50%
   of its current value.
   
   >>> image = load_image(choose_file()) 
   >>> reduce_red_50(image)
   >>> show(image)
   """
   for x, y, (r, g, b) in image:
      # decrease red component by 50%
      new_color = create_color(r * 0.5, g, b)
      set_color(image, x, y, new_color)
      
# Some functions to test the filters

def test_maximize_red():
   image = load_image(choose_file()) 
   show(image)    # display the unmodified image
   maximize_red(image)
   show(image)    # display the modified image
    
def test_reduce_red_50():
   image = load_image(choose_file()) 
   show(image)    # display the unmodified image
   reduce_red_50(image)
   show(image)    # display the modified image 
       
#-----------------------------------------------
# Put your solutions to Exercises 3 and 4 here.

def maximize_green(image):
   for x, y, (r, g, b) in image:
      new_color = create_color(r, 255, b)
      set_color(image, x, y, new_color)

def maximize_blue(image):
   for x, y, (r, g, b) in image:
      new_color = create_color(r, g, 255)
      set_color(image, x, y, new_color)
      
def reduce_green_50(image):
   for x, y, (r, g, b) in image:
      new_color = create_color(r, g * 0.5, b)
      set_color(image, x, y, new_color)

def reduce_blue_50(image):
   for x, y, (r, g, b) in image:
      new_color = create_color(r, g, b * 0.5)
      set_color(image, x, y, new_color)








   
      

