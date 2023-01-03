from fontTools.ttLib import TTFont

def get_char_list_from_ttf(font_file):
    ' 给定font_file,获取它的中文字符 '
    f_obj = TTFont(font_file)
    m_dict = f_obj.getBestCmap()
    unicode_list = []
    for key, _ in m_dict.items():
        unicode_list.append(key)
        
    char_list = [chr(ch_unicode) for ch_unicode in unicode_list]
    return char_list
 
font_file = "dataset\jinwen_ttf\jinwen.ttf"
chars = get_char_list_from_ttf(font_file)
# print(chars)