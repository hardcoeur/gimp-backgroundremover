#!/usr/bin/python2.7

from gimpfu import *
import subprocess
import os

def remove_background(image, drawable):
    # Save the current image to a temporary file
    temp_filename = '/tmp/temp_image.png'
    pdb.file_png_save_defaults(image, drawable, temp_filename, temp_filename)

    # Call the backgroundremover CLI tool
    subprocess.call(['backgroundremover', '-i', temp_filename, '-o', temp_filename])

    # Load the result back into GIMP
    new_layer = pdb.gimp_file_load_layer(image, temp_filename)
    image.add_layer(new_layer, 0)
    gimp.displays_flush()

    # Clean up the temporary file
    os.remove(temp_filename)

register(
    "python_fu_remove_background",
    "Remove Background",
    "Remove the background of an image using backgroundremover CLI tool",
    "Robert Renling",
    "Hardcoeur",
    "2023",
    "<Image>/Filters/Enhance/Remove Background...",
    "*",
    [],
    [],
    remove_background)

main()
