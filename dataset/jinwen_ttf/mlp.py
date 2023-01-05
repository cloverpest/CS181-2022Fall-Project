import json
import torch
import numpy as np
from torch.nn import Module, Linear, ReLU, MSELoss, Sigmoid, BCELoss
from torch.optim import SGD
from torch.nn.init import xavier_uniform_, kaiming_uniform_
from random import shuffle

def create_train_test(data):
    shuffle(data)
    train_data = data[:int(len(data) * 0.7)]
    test_data = data[int(len(data) * 0.7):]
    return train_data, test_data

class MLP(Module):
    def __init__(self, n_feature):
        super(MLP, self).__init__()
        self.hidden0 = Linear(n_feature, 40)
        kaiming_uniform_(self.hidden0.weight, nonlinearity='relu')
        self.act0 = ReLU()
        self.hidden1 = Linear(40, 15)
        kaiming_uniform_(self.hidden1.weight, nonlinearity='relu')
        self.act1 = ReLU()
        self.output = Linear(15, 1)
        xavier_uniform_(self.output.weight)
        self.act2 = Sigmoid()

        
    def forward(self, x):
        x = self.hidden0(x)
        x = self.act0(x)
        x = self.hidden1(x)
        x = self.act1(x)
        x = self.output(x)
        x = self.act2(x)
        return x

def train_model(train_data, model):
    criterion = BCELoss()
    optimizer = SGD(model.parameters(), lr=0.01, momentum=0.9)
    for epoch in range(100):
        for x, y in train_data:
            y_hat = model(torch.Tensor(x))
            loss = criterion(y_hat, torch.Tensor([y]))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print('epoch: {}, loss: {}'.format(epoch, loss.item()))
    return model

def test_model(test_data, model):
    correct = 0
    total = 0
    with torch.no_grad():
        for x, y in test_data:
            y_hat = model(torch.Tensor(x))
            if y_hat > 0.5:
                if y == 1:
                    correct += 1
            else:
                if y == 0:
                    correct += 1
            total += 1
    print('accuracy: {}'.format(correct / total))

bei = ['江南', '萧萧', '白云', '桃花', '梅花', '落花', '青山', '秋风', '清风', '黄花', '夕阳', '年年', '风雨', '桃李', '春风', '行人', '昨夜', '回首', '明月', '扁舟', '落日', '月明', '黄昏', '白发', '流水', '惆怅', '芙蓉', '长安', '东风', '天涯', '归去', '人家', '悠悠', '纷纷', '秋色', '寂寞', '春色', '花落', '黄叶']
ai = ['青山', '桃花', '春风', '秋声', '月明', '白云', '萧萧', '梅花', '秋风', '明月', '江南', '雨声', '落花', '流水', '风雨', '声中', '夕阳', '行人', '东风', '西风', '扁舟', '清风', '昨夜', '人家', '春色', '钟声', '纷纷', '分明', '归去', '年年', '回首', '歌声', '桃李', '寂寞', '黄昏', '君王', '山色', '落日', '夜半']
xi = ['江南', '白云', '梅花', '青山', '春风', '桃花', '萧萧', '流水', '春色', '明月', '桃李', '回首', '年年', '夕阳', '行人', '昨夜', '东风', '秋风', '落花', '人家', '归去', '芳草', '西湖', '月明', '扁舟', '纷纷', '风雨', '白头', '消息', '天涯', '长安', '寂寞', '青青', '惆怅', '江北', '黄昏', '白发', '红尘', '明日']
le = ['白云', '梅花', '江南', '桃花', '明月', '桃李', '春色', '春风', '落花', '年年', '行人', '芳草', '青山', '夕阳', '秋风', '回首', '白头', '江北', '流水', '长安', '纷纷', '扁舟', '君王', '寂寞', '燕子', '白发', '昨夜', '海棠', '青青', '天涯', '人家', '归去', '烟雨', '东风', '风流', '花落', '消息', '西湖', '风雨']
features = list(set(bei) | set(ai) | set(xi) | set(le))
# read poetry.json
independent_variable = []
dependent_variable = []
with open('poetry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
    for key, value in data.items():
        if value != -1:
            feature = []
            for f in features:
                if f in key:
                    feature.append(1)
                else:
                    feature.append(0)
            independent_variable.append(feature)
            dependent_variable.append(value)
data = []
for x, y in zip(independent_variable, dependent_variable):
    data.append((x, y))

train_data, test_data =  create_train_test(data)
model = MLP(len(features))
model = train_model(train_data, model)
test_model(test_data, model)




