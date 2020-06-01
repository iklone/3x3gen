# 3x3gen

A python generator for 3x3 composite images. Commonly used to collect and display a favourite list.

There are 2 scripts here:
- 3x3.py: Compile 9 images into a 3x3 composite image. Details below.
- jikan3x3.py: Grab data from a specified MyANimeList account and build a composite grid. Details below.

## 3x3.py

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
`python jikan3x3.py iklone characters`

8x8 grid of user iklone's top anime from his animelist:
`python jikan3x3.py iklone anime list 8`

5x5 grid of user iklone's favourite people with a grey border on a 10000x10000 pixel image:
`python jikan3x3.py iklone people fav 5 10000 128`
