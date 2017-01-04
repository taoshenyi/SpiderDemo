# coding=utf-8
'''
Created on 2017年1月4日

@author: xiaotao
'''
datas = []

data = {'title':'hello','url':'www.baidu.com'};

data1 = {'title':'hello','url':'www.baidu.com'};

datas.append(data);

datas.append(data1);

print datas

for das in datas:
    print das['title'];