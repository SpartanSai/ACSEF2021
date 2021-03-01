from PIL import Image, ImageOps
import numpy as np


for number in range(1,150):
    if number!=69 and number!=117:
        image = Image.open(r"/Users/saimonish/IntelliJ_workspace/ACSEF2021/Images/dutmc_09_{}.jpg".format(number)) 

        #target will be 870x484 pixels
        left = 734
        upper = 1080-484
        right = 1586
        lower = 1080

        image1 = image.crop((left,upper,right,lower))
        #image1 = ImageOps.grayscale(image1)
        image1 = image1.convert("LA")
        image1.save('/Users/saimonish/IntelliJ_workspace/ACSEF2021/CroppedImages/dutmc_09_{}_cropped.png'.format(number), "PNG")
        print("Save Successful!")
        
'''
image = Image.open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/CroppedImages/dutmc_09_1_cropped.png")
pixel_values = list(image.getdata())
'''