import numpy as np
import pandas as pd
import json
import math
path = 'D:/STU/大三上/AI/project/try/'

with open(path + 'train_new.json','r',encoding = 'utf-8') as fp:
    data_arr = fp.read().split('\n')
    label = []
    count = 0
    for datas in data_arr:
        data = json.loads(datas)
        if data['emotion'] == '悲':
            label.append(1)
        elif data['emotion'] == '喜':
            label.append(-0.1)
        count += 1
    weights = np.random.rand(count)
    #print(len(weights))
    #print(len(label))
    def logistic(wx):
        return 1.0 / (1.0+math.exp(-wx))
    label_ = []
    alpha = 0.8
    max_iteration = 10
    for i in range(max_iteration):
        count_ = 0
        for datas in data_arr:
            data = json.loads(datas)
            #print(count_,weights[count_]*label[count_])
            output = logistic(weights[count_]*label[count_])
            if weights[count_] * label[count_] >= 0:
                label_.append('悲')
            else:
                label_.append('喜')
            if label_[count_] == data['emotion']:
                continue
            else:
                if data['emotion'] == '悲':
                    weights[count_] = weights[count_] + alpha*(1-output)*label[count_]*output
                else:
                    weights[count_] = weights[count_] + alpha*(0-output)*label[count_]*output
            
            count_ += 1
        i += 1
    datalist = []
    
    num = 0
    right = 0
    wrong = 0
    for datas in data_arr:
        data = json.loads(datas)
        prob = logistic(weights[num]*label[num])
        if prob >= 0.5:
            datalist.append('悲')
        else:
            datalist.append('喜') 
        if datalist[num] == data['emotion']:
            right += 1
            print(data['title'],"right")
        else:
            wrong += 1
            print(data['title'],"wrong")
        num += 1
    #print (right/(right+wrong))
    timesbei = {'None' : 0}
    timesxi = {'None':-10000}
    num_ = 0
    for datas in data_arr:
        data = json.loads(datas)
        link = data['keywords'].split()
        for item in link:
            b = 1
            if data['emotion'] == '悲':
                b = weights[num_]
                timesbei[item] = b
                timesxi[item] = -10000
            else:
                b = -weights[num_]
                timesbei[item] = 0
                timesxi[item] = b
        num_ += 1
    timesbei = sorted(timesbei.items(),key=lambda x:x[1],reverse=True)
    timesxi = sorted(timesxi.items(),key=lambda x:x[1],reverse=False)
    timesbei = dict(timesbei)
    timesxi = dict(timesxi)
    print(list(timesbei.keys())[0:10])
    print(list(timesxi.keys())[1:11]) #!= 0
fp.close()
    