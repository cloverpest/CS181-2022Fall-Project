import jieba
import json

path = 'dataset/CCPC/'
listbei = ['江南','萧萧', '白云', '梅花', '清风', '秋风', '回首', '黄花',  '夕阳', '落花', '风雨',\
    '昨夜', '白发', '青山', '黄昏', '流水', '惆怅', '明月', '扁舟','落日', '悲秋', '芙蓉', '秋色', '春风', '长安']
listxi = ['江南', '白云', '青山',  '春风', '桃花', '流水', '明月', '年年', '东风', '桃李', '行人', '春色', '秋风', '夕阳', \
'西湖', '纷纷', '人家', '风雨', '月明', '白头',  '江北']
listai = ['青山',  '秋声', '白云', '梅花', '月明', '江南', '明月', '雨声', '萧萧', '秋风', '落花', '声中', '流水', '夕阳', '风雨', 
'东风', '清风', '行人', '扁舟', '春色', '西风', '钟声', '昨夜', '歌声', '人家', '归去', '黄昏']
listhuan = ['清风', '梅花', '桃李', '江南', '桃花', '白云', '春风', '年年', '合欢', '青山', '东风', '长安', '落花', '行人', '回首', '君王', '明月', 
'白头', '天涯',  '昨夜', '梨花', '黄金', '流水', '欢娱', '悠悠']
listle = ['梅花', '白云', '江南', '桃花', '行乐', '桃李', '春风', '春色', '年年', '回首', '乐事', '明月', '青山', '君王', '纷纷', '行人', 
'白头', '流水', '江北', '长安', '海棠', '芳草', '秋风', '扁舟',  '燕子', '白发', '青青']
listshang = ['伤心', '江南', '萧萧', '白云', '青山', '梅花', '行人', '春色', '春风', '夕阳', '风雨', '流水', '黄花', '芳草', '明月', '落花', '年年', 
'天涯', '回首', '桃花', '白发', '昨夜', '落日', '花落', '人家', '秋风', '扁舟', '伤春', '长安']
with open(path + 'ccpc_test_v1.0.json','r',encoding = 'utf-8') as fp:
    data_arr = fp.read().split('\n')
    for datas in data_arr:
        data = json.loads(datas)
        countbei = 0
        countxi = 0
        countai = 0
        counthuan = 0
        countle = 0
        countshang = 0
        for i in range(len(listbei)):
            if data['content'].find(listbei[i]) > 0:
                countbei += 1
        for i in range(len(listxi)):
            if data['content'].find(listxi[i]) > 0:
                countxi += 1
        for i in range(len(listai)):
            if data['content'].find(listai[i]) > 0:
                countai += 1
        for i in range(len(listhuan)):
            if data['content'].find(listhuan[i]) > 0:
                counthuan += 1
        for i in range(len(listle)):
            if data['content'].find(listle[i]) > 0:
                countle += 1
        for i in range(len(listshang)):
            if data['content'].find(listshang[i]) > 0:
                countshang += 1
        if countbei*30 + countai*10+countshang*1 > countxi*30+counthuan*1+countle*10:
            print('悲')
        elif countbei*30 + countai*10+countshang*1 < countxi*30+counthuan*1+countle*10:
            print('喜')
        elif countbei*30 + countai*10+countshang*1 == countxi*30+counthuan*1+countle*10:
            print('以乐景衬哀情')
fp.close()