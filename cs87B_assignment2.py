# -*- coding: utf-8 -*-
'''this program receives an image and changes the purple hues to green
and modifies the warm colors to make them cool, orange to blue. 
The resize function made the picture larger. The invert_colors function 
iterates through every pixel and applies the transformation.The end of the code
applies the change to the photo and saves the changes to a new file.
The new sizes are 900, and 40'''

from PIL import Image
import zipfile

def main():
  
    flor = Image.open("C:\\Users\\User1\\Downloads\\lavender.jpg")

    
    pix = flor.load()

    width, height = flor.size
    
    def invert_colors():
        for x in range(width):
            for y in range(height):
                r, g, b = pix[x, y]
                pix[x, y] = (255 - r, 255 - g, 255 - b)
            
        flor.save("flowerexperiment.jpg")

    def resize():
        new_width = 900
        new_height = 400

        new_size = (new_width, new_height)

        resized = flor.resize(new_size)

        resized.save("flowerresize.jpg")
        
        return resized

    invert_colors()
    resized_image = resize()

if __name__ == "__main__":
    main()

with zipfile.ZipFile("cs87Bassign2.zip", "w", zipfile.ZIP_DEFLATED) as myzip:
    myzip.write(__file__)   


        
            
        
        
        
        
    myzip.write(__file__)
