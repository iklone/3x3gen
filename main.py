import os
import sys
import time
from PIL import Image

def main(argv):
    imgList = []
    n = 0

    width = int(argv)
    sWidth = width // 3
    margin = 33

    for file in os.listdir("."):
        if file != '3x3.png' and (file.endswith(".png") or file.endswith(".jpg")):
            print(os.path.join(file))
            imgList.append(file)
            n += 1
            if n == 9:
                break
    
    img = Image.new('RGB', (width, width), (0, 0, 0))

    x = 0
    y = 0
    for file in imgList:
        img.save('3x3.png')
        time.sleep(0.2)
        #sys.exit()

        image = Image.open(file, 'r')
        image = image.resize((sWidth - margin, sWidth - margin))
        img.paste(image, (x * sWidth, y * sWidth, (x * sWidth) + sWidth - margin, (y * sWidth) + sWidth - margin))

        print ("inserted" + file)
        
        x += 1
        if x == 3:
            x = 0
            y += 1


    img.save('3x3.png')

if __name__ == "__main__":
    main(sys.argv[1])