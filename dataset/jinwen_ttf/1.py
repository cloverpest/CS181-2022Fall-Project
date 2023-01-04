
import json
 
#定义文件路径
path = 'D:/Shanghaitech/人工智能/CS181-2022Fall-Project/dataset/CCPC/'
patht = 'poetry.txt'
ci = '悲'
times = {'None':0}
 
# 打开文件,r是读取,encoding是指定编码格式
with open(path + 'ccpc_train_v1.0.json','r',encoding = 'utf-8') as fp:
 
    data_arr = fp.read().split('\n')
    # load()函数将fp(一个支持.read()的文件类对象，包含一个JSON文档)反序列化为一个Python对象
    #for datas in data_arr:
        #data = json.loads(datas)  #输出结果是 <class 'dict'> 一个python对象,json模块会根据文件类对象自动转为最符合的数据类型,所以这里是dict
        #if data['content'].find('悲'):
            
            #print(data['keywords'])
    for datas in data_arr:
        data = json.loads(datas)
        if data['content'].find(ci)!=-1:
            link = data['keywords'].split()
            for item in link:
                b = 0
                for key in times:
                    if key == item and item != ci:
                        times[item] += 1
                        b = 1
                if b == 0 and item != ci:
                    times[item] = 1
    times = sorted(times.items(), key=lambda x: x[1],reverse=True)
    times = dict(times)
    for ci2 in list(times.keys())[0:19]:
        for datas in data_arr:
            data = json.loads(datas)
            if data['content'].find(ci2)>0:
                link = data['keywords'].split()
                for item in link:
                    b = 0
                    for key in times:
                        if key == item and item != ci2:
                            times[item] += 1
                            b = 1
                    if b == 0 and item != ci2:
                        times[item] = 1
    times2 = sorted(times.items(), key=lambda x: x[1],reverse=True)
    times2 = dict(times2)
    for ci2 in list(times.keys())[0:29]:
        for datas in data_arr:
            data = json.loads(datas)
            if data['content'].find(ci2)>0:
                link = data['keywords'].split()
                for item in link:
                    b = 0
                    for key in times:
                        if key == item and item != ci2:
                            times[item] += 1
                            b = 1
                    if b == 0 and item != ci2:
                        times[item] = 1
    times2 = sorted(times.items(), key=lambda x: x[1],reverse=True)
    times2 = dict(times2)
    for ci2 in list(times.keys())[0:29]:
        for datas in data_arr:
            data = json.loads(datas)
            if data['content'].find(ci2)>0:
                link = data['keywords'].split()
                for item in link:
                    b = 0
                    for key in times:
                        if key == item and item != ci2:
                            times[item] += 1
                            b = 1
                    if b == 0 and item != ci2:
                        times[item] = 1
    times2 = sorted(times.items(), key=lambda x: x[1],reverse=True)
    times2 = dict(times2)
    print(list(times2.keys())[0:39])

    output = []
    for gci in list(times2.keys())[0:39]:
        for datas in data_arr:
            data = json.loads(datas)
            if data['keywords'].find(gci)>0:
                if output.count(data['content']) == 0:
                    output.append(data['content'])
fp.close()
f = open(patht,'w',encoding='utf-8')
for item in output:

    if not f.write(item+'\n'):
        continue

f.close()