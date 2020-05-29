import os
import sys
import time
from PIL import Image

def main(width, brightness):
    imgList = []
    n = 0

    margin = width // 100
    sWidth = (width - (4 * margin)) // 3
    uWidth = sWidth + margin

    for file in os.listdir("."):
        if file != '3x3.png' and (file.endswith(".png") or file.endswith(".jpg")):
            imgList.append(file)
            n += 1
            if n == 9:
                break
    
    imgList.sort()
    print(imgList)

    img = Image.new('RGB', (width, width), (brightness, brightness, brightness))

    x = 0
    y = 0
    for file in imgList:
        image = Image.open(file, 'r')

        origWidth = image.size[0]
        origHeight = image.size[1]
        if origWidth > origHeight:   # if landscape
            cropped = (origWidth - origHeight) // 2
            image = image.crop((cropped, 0, cropped + origHeight, origHeight))
        else:                           # if portrait
            cropped = (origHeight - origWidth) // 2
            image = image.crop((0, cropped, origWidth, cropped + origWidth))

        image = image.resize((sWidth, sWidth))

        img.paste(image, ((x * uWidth) + margin, (y * uWidth) + margin))

        print (file)
        
        x += 1
        if x == 3:
            x = 0
            y += 1


    img.save('out.png')

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))