import os
import sys
import time
from PIL import Image
from jikanpy import Jikan
import json
import urllib.request
import random
from random import randrange

#return images for all x in fav list lType
def jikanGetFav(username, lType, imgList):
    jikan = Jikan()

    user = jikan.user(username)

    for favourite in user["favorites"][lType]:
        print(favourite["name"])
        imgList.append(favourite["image_url"])

#return images for all x in list of rating score
def jikanGetList(username, lType, matrix, imgList, score):
    if not(lType == 'anime' or lType == 'manga'):
        print("Cannot compile favourite " + lType + " image from option 'list', use option 'fav' instead")
        quit()
    
    jikan = Jikan()

    user = jikan.user(username, "" + lType + "list", parameters={'order_by' : 'score', 'sort' : 'desc'})

    for anime in user[lType]:
        if anime["score"] == score:
            imgList.append(anime["image_url"])
            print(anime["title"])
    
    print("List length = " + str(len(imgList)))

#insert all of imgList into img
def insert(img, imgList, fMatrix, margin, sWidth, uWidth, done):
    loc = 0
    for file in imgList:
        #find open spot
        while True:
            loc = randrange(matrix * matrix)
            if fMatrix[loc]:
                break

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

        fMatrix[loc] = 0
        done += 1
        if done == (matrix * matrix):
            break

def main(username, lType, favKA, matrix, width, brightness):
    imgList = []
    n = 0

    margin = width // (30 * matrix)
    sWidth = (width - (matrix * margin)) // matrix
    uWidth = sWidth + margin

    img = Image.new('RGB', ((uWidth * matrix) + margin, (uWidth * matrix) + margin), (brightness, brightness, brightness))
    fMatrix = [1] * (matrix * matrix)

    done = 0
    if favKA: #if from fav list
        jikanGetFav(username, lType, imgList)
        random.shuffle(imgList)
        insert(img, imgList, fMatrix, margin, sWidth, uWidth, done)
    else: # if from anime/mangalist
        score = 10
        while True:
            print("Score = " + str(score))
            imgList = []
            jikanGetList(username, lType, matrix, imgList, score)
            random.shuffle(imgList)
            insert(img, imgList, fMatrix, margin, sWidth, uWidth, done)

            score = score - 1
            done += len(imgList)
            if done >= (matrix * matrix):
                break

    img.save('Jout.png')
    #img.show()

if __name__ == "__main__":
    argLen = len(sys.argv)
    lType = 'anime'
    favKA = 1
    matrix = 3
    width = 1000
    borderB = 0

    #load help
    if (argLen == 1):
        print("""Welcome to 3x3gen. Use to generate anime XxXs from MAL
Arguments:
username (anime/manga/characters/people, default anime) (fav/list, default fav) (matrix width) (image pixel size) (border brightness) """)
        quit()

    #load username
    username = sys.argv[1]

    #type: anime/manga/people/characters
    if (argLen >= 3):
        lType = sys.argv[2]

    #from favs or list
    if (argLen >= 4):
        if sys.argv[3] == 'list':
            favKA = 0

    #matrix size
    if (argLen >= 5):
        matrix = int(sys.argv[4])
        if matrix < 1 or matrix > 17:
            print("Grid can be minimum 1 wide and maximum 17 wide")
            quit()

    #image size
    if (argLen >= 6):
        width = int(sys.argv[5])

    #border brightness
    if argLen == 7:
        borderB = int(sys.argv[6])

    print("Loading a " + str(matrix) + "x" + str(matrix) + " from " + username + "'s favourite " + lType + " list")
    print("Generate from favourites = " + str(bool(favKA)))
    print()
    main(username, lType, favKA, matrix, width, borderB)