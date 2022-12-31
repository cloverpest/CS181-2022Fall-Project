from fontTools.ttLib import TTFont
from fontTools.pens.freetypePen import FreeTypePen
from fontTools.misc.transform import Offset
from PIL import Image

pen = FreeTypePen(None) # 实例化Pen子类
font = TTFont("dataset\jinwen_ttf\jinwen.ttf") # 实例化TTFont
glyph = font.getGlyphSet()["uni9C9B"] # 通过字形名称选择某一字形对象
glyph.draw(pen) # “画”出字形轮廓
width, ascender, descender = glyph.width, font['OS/2'].usWinAscent, -font['OS/2'].usWinDescent # 获取字形的宽度和上沿以及下沿
height = ascender - descender # 利用上沿和下沿计算字形高度
pen.show(width=width, height=height, transform=Offset(0, -descender)) # 显示以及矫正
img = pen.image(width=width, height=height,transform=Offset(0, -descender))
img.save("1.png")