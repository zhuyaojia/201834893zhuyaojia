# -*- coding: utf-8 -*-
import os
import random
import math
#import sklearn.cross_validation
#将数据集分成训练集和数据集，从每个文件夹中抽取80%作为训练集，20%作为测试集，最后得到总的训练集train，测试集test，每个元素都是文件的名字
def trainTestSplit(X, test_size=0.2):
           X_num = len(X)#所有文件数量
           train_num=int(X_num*(1-test_size))#训练集文件数量
          # train_index = range(train_num)
           #test_index = range(test_num)
           train=[]
           test=[]
           for i in range(train_num):
                train.append(X[i])
           for j in range(train_num+1,X_num):
                test.append(X[j])
           return train, test
#得到每个文件夹下的所有文件
def getlist(tmp_path):
        filess=os.listdir(tmp_path)#读取一个文件夹下的所有文件名
        return filess
def dividedata(dataset):
    dataset_num=len(dataset)
    data_list=[]
   #打开训练集下所有文件(一个文件夹下的)
    for j in range(dataset_num):
       file_path = os.path.join(tmp_path + "\\" + dataset[j])
       data_list=detaildividedata(file_path)
    return data_list
#具体分词
def dividealldata(alist):
    dataset_num=len(alist)
    data_list=[]
   #打开训练集下所有文件(一个文件夹下的)
    for j in range(dataset_num):
        list_num = len(alist[j])
        dataset=alist[j]
        for i in range(list_num):
            docu_size = len(dataset[i])
            file_path = os.path.join(patha + "\\" + dataset[j])
            data_list=detaildividedata(file_path)
    return data_list
def detaildividedata(path):
    data_list=[]
    f = open(path, 'r')  # 打开一个文件
    str = f.read()
    word_list = str.split()
    # 处理一个文件
    for word1 in word_list:
        wordss = word1.strip(':().,"@`-;><!?_[]')
        word = wordss.strip("'")
        if (len(word) != 0):
            data_list.append(word)
    return data_list

def createVocabList(datalist):  #创建词库 这里就是直接把所有词去重后，当作词库
    vocablist = []
    data_len=len(datalist)
    for i in range(data_len):
        if datalist[i] not in vocablist:
             vocablist.append(datalist[i])
    return vocablist
def setOfWords2Vec(vocabList):#文本词向量。词库中每个词当作一个特征，文本中就该词，该词特征就是1，没有就是0
    train_vec_list=[]
    returnVec = [0] * len(vocabList)#returnVec是零矩阵
    data_list=dividealldata(alist)
    for word in data_list:
            if word in vocabList:
                returnVec[vocabList.index(word)] += 1
                train_vec_list.append(returnVec)
    return train_vec_list
#训练模型
def trainNB0(train_vec):
    #获得训练集中单词个数
    numWords = len(train_vec)
    #所有类别个数
    allclass=len(list)
    #计算文档属于文件夹名字类的概率
    pAbusive = 1 / float(allclass)
    p1Num=0
    p0Num=0
    p0Num_list = []#一个词语没在文档中出现的次数
    p1Num_list = []#一个词语在所有文档中出现的次数：
    #p0Denom = 2
    #p1Denom = 2
    p1Vect=[]
    p0Vect=[]
    word_sum=0
    #遍历训练向量的所有词汇
    for i in range(numWords):
        inter_num=len(train_vec[i])
        inter_list=train_vec[i]
        for j in range(inter_num):
            #该词出现在文档中
            if inter_list[j] >0:
                p1Num+=inter_list[j]
                word_sum+=p1Num
                p1Num_list.append(p1Num)
            else:
               #该词不出现在文档中
                p0Num += 1
                p0Num_list.append(p0Num)
    for k in range(numWords):
        p1Vect.append(float(p1Num_list[k]) /float( word_sum))
        p0Vect.append(float(p0Num_list[k]) / float(word_sum))
    return p1Vect, p0Vect,pAbusive
#分类函数
def classifyNB(train_vec, p0Vec, p1Vec, pclass):
    numWords = len(p1Vect)
    p1 = p0 = 0
    for i in range(numWords):
        p1 = p1 + math.log(p1Vect[i])
        p0 = p0 + math.log(p0Vect[i])
    p1 = p1 + math.log(pclass)
    p0 = p0 + math.log(1 - pclass)
    # 分类结果
    if p1 > p0:
        return 1#属于文件夹类
    else:
        print 0;#不属于文件夹类

patha = "D:\\homework2\\20news-18828" #文件夹目录
files= os.listdir(patha) #得到文件夹下的所有文件夹名称
word_list = []
filess=[]
words=[]
str=""
train=[]#训练集所有文件的名字
test=[]#测试集所有文件的名字
train_vocab=[]
test_vocab=[]
filelist_num= len(files)
#分词后的集合
alist=[]#所有文档名的列表
train_vec=[]#训练集的向量表示
test_vec=[]#测试集的向量表示
p1Vect=[]#训练集每个词出现的频率
p0Vect=[]#训练集每个词未出现的频率
atrain=[]#总的训练集(文件名)
atest=[]#总的测试集
for i in range(filelist_num):
    #处理一个文件夹下的所有文件
    tmp_path = os.path.join(patha + "\\" + files[i])
    list=getlist(tmp_path)
    alist.append(list)
    train, test =trainTestSplit(list, test_size=0.2)
#得到训练集和测试集的分词
    train_data=dividedata(train)
    atrain.append(train_data)
    test_data=dividedata(test)
    atest.append(test_data)
train_vocab=createVocabList(atrain)
test_vocab=createVocabList(atest)
#train_vec=setOfWords2Vec(train_vocab)
data_list=[]
#打开训练集下所有文件(一个文件夹下的)
list_num=len(alist)
for j in range(list_num):
    docu_size=len(alist[j])
    dataset=alist[j]
    for i in range(docu_size):
        file_path = os.path.join(tmp_path + "\\" + dataset[i])
        data_list=detaildividedata(file_path)
    print data_list
#返回每个词的概率向量和属于某个类的概率)
#p1Vect,p0Vect,pclass=trainNB0(train_vec)
#test_vec.append(setOfWords2Vec(test_vocab))
#训练效果
#p=classifyNB(train_vec,p1Vect,p0Vect,pclass)
#print p
#测试
#print train_data
