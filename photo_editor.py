# SYSC 1005 A Fall 2017 Lab 7

import sys  # get_image calls exit

from Cimpl import *

from filters import *

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
    
        
    
    
