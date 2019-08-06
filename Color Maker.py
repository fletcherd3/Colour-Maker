'''

Created by Fletcher Dick on 4th Aug 19.
This is a quick script i made to generate a whole bunch of colours, I wanted to
have my background constantly changing colour using the mac auto background
refresh thing but I couldn't find a download of a lot of colours.
The advantage of making this was I could choose exactly how many colours I 
wanted and the size of the image.
I found the minimum size I could use was 2x2px so I used this to speed up the
time.

'''

from PIL import Image # Import PIL to use in saving images.

skip_amount = 10 # This is the amount each value iterates up by.
                 # 10 makes around 17,000 images.
max_rgb = 255 # Decrease if you want darker colours

red = None
green = None
blue = None

# Loop through the RGB values while skipping a amount of 'skip_amount'.
for red in range(0, max_rgb + 1, skip_amount):
    for green in range(0, max_rgb + 1, skip_amount):
        for blue in range(0, max_rgb + 1, skip_amount):
            # Create 2x2px image with given RGB values
            img = Image.new('RGB', (2, 2), (red, green, blue))
            
            img.save("/Users/FletcherDick/Pictures/Colours/{},{},{}.jpg"
                     .format(red, green, blue)) # Save images to folder

