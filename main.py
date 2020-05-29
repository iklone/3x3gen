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
    
    img = Image.new('RGB', (width, width), (brightness, brightness, brightness))

    x = 0
    y = 0
    for file in imgList:
        image = Image.open(file, 'r')
        image = image.resize((sWidth, sWidth))
        img.paste(image, ((x * uWidth) + margin, (y * uWidth) + margin, (x + 1) * uWidth, (y + 1) * uWidth))

        print (file)
        
        x += 1
        if x == 3:
            x = 0
            y += 1


    img.save('3x3.png')

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))