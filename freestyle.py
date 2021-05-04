import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont
from jikanpy import Jikan
import json
import urllib.request
import random
from random import randrange
import math

def searchMAL(title, imgList, sleep):
    jikan = Jikan()

    result = jikan.search('anime', title)
    firstResult = result["results"][0]
    imgList.append(firstResult["image_url"])
    print(firstResult["title"])
    time.sleep(sleep)

#insert all of imgList into img
def insert(img, imgList, matrix, count, margin, sWidth, uWidth, done):
    loc = 0
    for file in imgList:

        image = Image.open(urllib.request.urlopen(file), 'r')

        origWidth = image.size[0]
        origHeight = image.size[1]
        if origWidth > origHeight:   # if landscape
            cropped = (origWidth - origHeight) // 2
            image = image.crop((cropped, 0, cropped + origHeight, origHeight))
        else:                           # if portrait
            cropped = (origHeight - origWidth) // 2
            image = image.crop((0, cropped, origWidth, cropped + origWidth))

        image = image.resize((sWidth, sWidth), Image.ANTIALIAS)

        y = loc // matrix
        x = loc % matrix
        print(str(done + 1) + "/" + str(matrix*matrix) + " : " + "(" + str(x) + ", " + str(y) + ")")
        img.paste(image, ((x * uWidth) + margin, (y * uWidth) + margin))

        #print (file)

        #img.save('Jout.png')
        #time.sleep(0.5)

        done += 1
        loc += 1
        if done == count:
            break

def main(file, title, matrixW, width, brightness, randomise):
    imgList = []
    n = 0

    done = 0
    F = open(file, "r")
    count = len(open(file, "r").readlines())
    if (count > 30):
        sleep = 2
    else:
        sleep = 1.5
    print("File \"" + file + "\" has " + str(count) + " entries.")
    matrixH = math.ceil(count / matrixW)

    print("Building matrix of " + str(matrixW) + "x" + str(matrixH) + ".")
    print("This will take around " + str(5 + (count * sleep)) + "s.")
    print()
    F.close()

    F = open(file, "r")
    for atitle in F:
        searchMAL(atitle, imgList, sleep)
    F.close()

    print()

    margin = width // (30 * matrixW)
    sWidth = (width - (matrixW * margin)) // matrixW
    uWidth = sWidth + margin

    img = Image.new('RGB', ((uWidth * matrixW) + margin, (uWidth * matrixH) + margin), (brightness, brightness, brightness))

    if (randomise) :
        random.shuffle(imgList)

    insert(img, imgList, matrixW, count, margin, sWidth, uWidth, done)

    #Insert title
    if (title != "false"):
        print("Inserting title \"" + title + "\"")
        timg = Image.new('RGB', ((uWidth * matrixW) + margin, (uWidth * matrixH) + margin + 50), (brightness, brightness, brightness))
        tdraw = ImageDraw.Draw(timg)
        font = ImageFont.truetype("font.ttf", 50)
        tdraw.text((margin + 0,0), title, font=font)

        timg.paste(img, (0, 50))
        img = timg

    img.save('Fout.png')
    #img.show()

if __name__ == "__main__":
    argLen = len(sys.argv)
    title = "false"
    width = 1000
    borderB = 0
    randomise = 0
    matrixW = 3

    #load help
    if (argLen == 1):
        print("""Welcome to 3x3gen manual edition. Use to generate anime XxXs from MAL
Arguments:
filename (grid title) (matrix width) (random order: true/false) (image pixel width) (border brightness) """)
        
        quit()

    #load filename
    file = sys.argv[1]

    #load grid title
    if (argLen >= 3):
        title = sys.argv[2]

    #matrix size
    if (argLen >= 4):
        matrixW = int(sys.argv[3])
        if matrixW < 1:
            print("Grid can be minimum 1 wide")
            quit()

    #randomise
    if (argLen >= 5):
        randomiseInput = str(sys.argv[4])
        if (randomiseInput == "true") :
            randomise = 1

    #image size
    if (argLen >= 6):
        width = int(sys.argv[5])

    #border brightness
    if argLen == 7:
        borderB = int(sys.argv[6])

    print("Loading from " + file)
    print()
    main(file, title, matrixW, width, borderB, randomise)