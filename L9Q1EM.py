# ----------------------------------------
# All of the work is mine.
#- Essey
# ----------------------------------------
# Name:     Essey
# Program:  L9Q1EN.py
# ----------------------------------------
# Purpose: 
# Fix a stop sign image that is "broken"		
# ----------------------------------------

from PIL import Image
picture = Image.open("stop_colored.png")

# Corrects the centre section by converting green to red and cyan to magenta.
def fix_middle(picture):
    
    w, h = picture.size   
    x_start = int(w * 0.25)   
    x_stop = int(w * 0.75)     
      
    for y in range(h):
        for x in range(x_start, x_stop):
            r,g,b = picture.getpixel((x, y))
            picture.putpixel((x, y), (g,r,b) )    
    return picture

# Changes yellow pixels to white.
def fix_top_half(picture):
    w, h = picture.size 
    y_start = 0
    y_end = int(h * 0.5)
    yellow = (255, 255, 0)
    white = (255, 255, 255)    
    for y in range(h):
        for x in range(w):
            colour = picture.getpixel((x, y))
            if (colour == yellow):
                picture.putpixel((x, y), white)    
    return picture

# Replaces the magenta rectangle with a new rectangle that moves from black to blue.
def make_rect_varyh(picture):
    w, h = picture.size 
    x_start = int(w * 0.1)
    y_start = int(h * 0.7)
    x_end = int( x_start + (w * 0.8))
    y_end = int(y_start + (h * 0.051))
    colour_count = 0
    for x in range(x_start, x_end, 1):
        for y in range(y_start, y_end, 1):
            picture.putpixel((x, y), (0, 0, colour_count))
        colour_count += 1
    return picture

# The program's main function which calls all of the others
def fix_file(file_name):
    fix_middle(picture)
    fix_top_half(picture)
    make_rect_varyh(file_name)
fix_file(picture)
picture.show()

