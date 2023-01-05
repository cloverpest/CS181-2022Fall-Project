import json
from random import shuffle

def create_train_test(data):
    shuffle(data)
    train_data = data[:int(len(data) * 0.7)]
    test_data = data[int(len(data) * 0.7):]
    return train_data, test_data

# train by Naive Bayes
def train(train_data):
    # calculate the probability of each class
    total = len(train_data)
    count = [0, 0]
    for x, y in train_data:
        count[y] += 1
    prob = [c / total for c in count]
    
    # calculate the probability of each feature in each class
    feature_count = [[0] * len(features) for i in range(2)]
    for x, y in train_data:
        for i in range(len(features)):
            feature_count[y][i] += x[i]
    feature_prob = [[0] * len(features) for i in range(2)]
    for i in range(2):
        for j in range(len(features)):
            feature_prob[i][j] = (feature_count[i][j] + 1) / (count[i] + 2)
    return prob, feature_prob

# predict by Naive Bayes
def predict_evaluate(test_data, prob, feature_prob):
    # print('feature_prob: ', feature_prob)
    error = 0
    for x, y in test_data:
        prob1 = prob[1]
        prob0 = prob[0]
        for i in range(len(features)):
            if x[i] == 1:
                prob1 *= feature_prob[1][i]
                prob0 *= feature_prob[0][i]
        if prob1 > prob0 and y == 0:
            error += 1
        elif prob1 < prob0 and y == 1:
            error += 1
    return error / len(test_data)


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
prob, feature_prob = train(train_data)
error_rate = predict_evaluate(test_data, prob, feature_prob)
print('error_rate: ', error_rate)