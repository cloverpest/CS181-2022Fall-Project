import json
from collections import Counter
import math
import numpy as np
import tensorflow as tf
path = 'dataset/CCPC/'

disallowed = ['(',')','__','[',']','【','】']
max_len = 66
min_frequency = 6
batch_size = 16

poetry = []
with open(path + 'poetry.txt','r',encoding = 'utf-8') as fp:
    lines = fp.readlines()

for line in lines:
    if line.count(':') == 1:
        title,content = line.split(':')
        flag = False
        #调整格式一致
        for word in disallowed:
            if word in content:
                flag = True
        if flag:
            continue
        if len(content) > max_len:
            continue
        poetry.append(content.replace('\n',''))
        
#词频
counter = Counter()
for line in poetry:
    counter.update(line)
token_=[]   
for tok,count in counter.items():
    if count >= min_frequency:
        token_.append((tok,count))
token_ = sorted(token_,key=lambda x: -x[1])
for tok,count in token_:
    token_.append(tok)
token_ = ['[STRING]','[LOW_FRE]','[START]','[END]']+token_
token_len = len(token_)
token_to_dict = dict(zip(token_,range(token_len)))
class toker:
    def __init__(self,token_dict):
        self.token_dict = token_dict
        for key,value in self.token_dict.items():
            self.token_dict_re = {value:key}
        self.token_len = len(self.token_dict)
    def token_id(self,token):
        return self.token_dict.get(token,self.token_dict['[LOW_FRE]'])
    def id_token(self,token_id):
        return self.token_dict_re[token_id]
    def decode(self,token_id):
        tokens = []
        for id in token_id:
            token = self.id_token(id)
            if token not in {'[START]','[END]'}:
                tokens.append(token)
            else:
                continue
        return ''.join(tokens)
    def encoding(self,tokens):
        token_ids = [self.token_id('[START]'),]
        for token in tokens:
            token_ids.append(self.token_id(token))
        token_ids.append(self.token_id('[END]'))
        return token_ids
        
        
