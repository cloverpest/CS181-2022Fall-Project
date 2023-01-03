import os
#read png from folder
def read_png(path):
    path = "font/"
    file_list = os.listdir(path)
    char_list = []
    for file in file_list:
        if not os.path.isdir(file):
            char_list.append(file)
    return char_list
path = "font/"
#open a png and output its pixel
from PIL import Image
def get_pixel(path):
    img = Image.open(path)
    width, height = img.size
    pixel = img.load()
    for x in range(round(-width/8), round(width/8)):
        has_line = True
        for y in range(height):
            if pixel[round(width/2)+x, y][1] != 0:
                has_line = False
        if has_line:
            # divide the png by x value
            img1 = img.crop((0, 0, round(width/2)+x, height))
            img2 = img.crop((round(width/2)+x, 0, width, height))
            # split path by "."
            filename = (path.split("/"))[-1]
            img1.save("left_right/"+"left_"+filename)
            img2.save("left_right/"+"right_"+filename)
            
    for y in range(round(-height/8), round(height/8)):
        has_line = True
        for x in range(width):
            if pixel[x, round(height/2)+y][1] != 0:
                has_line = False
        if has_line:
            # divide the png by y value
            img1 = img.crop((0, 0, width, round(height/2)+y))
            img2 = img.crop((0, round(height/2)+y, width, height))
            # split path by "."
            filename = (path.split("/"))[-1]
            img1.save("up_down/"+"up_"+filename)
            img2.save("up_down/"+"down_"+filename)

# make up_down folder and left_right folder empty


pngs = read_png(path)
for i in range(150,500):
    get_pixel(path+pngs[i])