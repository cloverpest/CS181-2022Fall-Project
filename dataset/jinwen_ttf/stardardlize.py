import skimage.io as io
from PIL import Image
import os
def alpha2white(img):
    img = img.convert("RGBA")
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if img.getpixel((x,y))[3] == 0:
                img.putpixel((x,y),(255,255,255,255))
    return img
def stardardlize(path):
    im = Image.open(path)
    im = alpha2white(im)
    im.convert("L")
    im.save("temp.png")
    # im.show()
    img_io = io.imread("temp.png")
    alpha = img_io[:,:,0]
    alpha = (alpha == 0) * 255
    resolution = [50, 50]
    font_size = 48
    output = Image.fromarray(alpha)
    #output = output.convert("L")
    #output.show()
    scale = font_size / max(output.size[0], output.size[1])
    resize_width = int(output.size[0] * scale)
    resize_height = int(output.size[1] * scale)
    output = output.resize((resize_width, resize_height), Image.Resampling.LANCZOS)
    final_img = Image.new("L", resolution)
    final_img.paste(output, (int((resolution[0] - output.size[0])/2),int((resolution[1] - output.size[1])/2)))
    final_img.save("standardlized/" + path)
paths = ["uni4EBA/", "uni6C34/", "uni7A0B/", "uni7AF9/", "uni7C7D/", "uni7E83/"]
for path in paths:
    for f in os.listdir(path):
        stardardlize(path+f)
