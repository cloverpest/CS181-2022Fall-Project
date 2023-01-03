from fontTools.ttLib import TTFont
from fontTools.pens.freetypePen import FreeTypePen
from fontTools.misc.transform import Offset
from PIL import Image
def get_pic_and_dict(font_file, need_save=True):
    f_obj = TTFont(font_file)
    m_dict = f_obj.getBestCmap()
    unicode_list = []
    for key, value in m_dict.items():
        unicode_list.append(key)
        if need_save:
            pen = FreeTypePen(None) # 实例化Pen子类
            glyph = f_obj.getGlyphSet()[value] # 通过字形名称选择某一字形对象
            glyph.draw(pen) # “画”出字形轮廓
            width, ascender, descender = glyph.width, f_obj['OS/2'].usWinAscent, -f_obj['OS/2'].usWinDescent # 获取字形的宽度和上沿以及下沿
            height = ascender - descender # 利用上沿和下沿计算字形高度
            #pen.show(width=width, height=height, transform=Offset(0, -descender)) # 显示以及矫正
            img = pen.image(width=width, height=height,transform=Offset(0, -descender))
            img.save("font/"+value+".png")
    char_list = [chr(ch_unicode) for ch_unicode in unicode_list]
    # create dict which maps char to unicode
    char_dict = {}
    for i in range(len(char_list)):
        char_dict[char_list[i]] = unicode_list[i]
    return char_dict
font_file = "dataset\jinwen_ttf\jinwen.ttf"
char_dict = get_pic_and_dict(font_file)