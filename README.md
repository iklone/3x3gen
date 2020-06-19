# 3x3gen

A python generator for 3x3 composite images. Commonly used to collect and display a favourite list.

There are 3 scripts here:
- 3x3.py: Compile 9 images into a 3x3 composite image. Details below.
- jikan3x3.py: Grab data from a specified MyANimeList account and build a composite grid. Details below.
- jikanman3x3.py: Uses a list pulled from a text file to build a grid using MAL images. Details below.

## 3x3.py

### Requirements

For both scripts:

- Python 3
- PIL: `pip install pil`

For jikan3x3.py:

- jikanpy: `pip install jikanpy`

### Use

To use the program, place the 3x3.py file in a directory/folder with the 9 images you want to compile. Then run from command line with 2 arguments:

1. Size: width/height in pixels, image is always square. (integer) (default 1000)
2. Border: Grey value of the border. 0 for black, 255 for white. (integer) (default black)

## Function

The program will order the images by filename and place the in the configuration:

```
1 2 3
4 5 6
7 8 9
```

Images other than the first 9 (alphabetically) in the directory will be ignored. Recognises .jpg, .jpeg and .png files.

### Examples

3x3 using images in directory. 1000x1000 pixels and a black border (default)
`python 3x3.py`

Image of 10000x10000 pixels with grey border:
`python 3x3.py 10000 128`

## jikan3x3.py

### Use

Can be run anywhere, will generate image into current directory.

Arguments:

1. Username: MAL username (string) **REQUIRED**
2. Type: Type of favourite list: anime/manga/characters/people (string) {default anime)
3. Datapool: Where the data is pulled from: fav/list (Fav pulls from the "favorites" section of your about page. list pulls from either your animelist or your mangalist). Manga/anime grids can use fav or list. Character/people grids **MUST** use fav. (string) (default fav)
4. Matrix width: Width/Height of the grid. To build a 3x3 (9 total items) use 3. (integer) (default 3)
5. Image width: Width of the output image in pixels. (integer) (default 1000)
6. Border brightness: Grey value of the border. 0 for black, 255 for white (integer) (default black)

### Function

The items will be placed into the grid in a random configuration.

If datapool = list, items will be placed in in order of "score". Sub-score order is randomised. For example, if running a 5x5 anime grid, but there are only 20 anime rated 10/10, 5 9/10 anime will be chosen at random to fill in the gaps.

While there is nothing preventing it, grids using datapool fav only have a pool size of 10. Therefore 3x3 grids are the maximum size fillable grids.

### Examples

3x3 grid of user iklone's favourite characters:
`python3 jikan3x3.py iklone characters`

8x8 grid of user iklone's top anime from his animelist:
`python3 jikan3x3.py iklone anime list 8`

5x5 grid of user iklone's favourite people with a grey border on a 10000x10000 pixel image:
`python3 jikan3x3.py iklone people fav 5 10000 128`

## jikanman3x3.py

### Use

Must be sent a plain text file containing the wanted anime, one per line without any blank lines. This file must be sent through the first argument.

Arguments:

1. File: Directory of text file (directory) **REQUIRED**
2. Title: Grid title. Will be inserted above grid on image. (string)
3. Custom matrix size: Custom matrix width. Will be automatically calculated otherwise. (integer)
4. Image width: Width of the output image in pixels. (integer) (default 1000)
5. Border brightness: Grey value of the border. 0 for black, 255 for white (integer) (default black)

### Function

The items order will be randomised, and then inserted into a grid. The size of the grid is eithe manually inputted or calculated from the floor of the square root of the number of items. This means that some items may be cut out if the given list's length isn't a square number. The items cut will be randomised each run.

The grid title requires a \*.ttf file to be present in the directory. Find the truetype font of your choosing and place it into the directory you are running the script. The title's size and position is currently non-customisable. If you are having trouble here it may be easier to manually add the title afterwards in an image editor. The font I use is *VCR OSD Mono Regular*, and can be found online for free.

### Examples

3x3 grid of "miyazaki.txt" with title "Miyazaki Anime". Since example.txt has 10 items, and 3^2=9, one item will be randomly cut.
`python3 jikanman3x3.py miyazaki.txt "Miyazaki Anime"`

Using file "miyazaki.txt":
```
Spirited Away
Ponyo
Nausicaa
Panda Kopanda
Lupin III Cagliostro
Kiki's Delivery Service
Princess Mononoke
Future Boy Conan
Laputa
Totoro
```
