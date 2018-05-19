#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  numpy as np
import operator as op
import matplotlib.pyplot as plt


def createDataSet():
    group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    # print(group.shape)
    labels=['A','A','B','B'];
    return  group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0];
    diffMat=np.tile(inX,[dataSetSize,1])-dataSet
    sqDiffMat=diffMat**2;
    distance=sqDiffMat.sum(axis=1)**0.5
    sortDistIndices=distance.argsort();
    classCount={};
    for i in range(k):
        voteIlabel=labels[sortDistIndices[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        # print(classCount.get(voteIlabel,0))
    sortedClassCount=sorted(classCount.items(),key=op.itemgetter(1),reverse=True)
    print(classCount.items());
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr=open(filename)
    lines=fr.readlines()
    numberLines=len(lines)
    returnMat=np.zeros((numberLines,3))
    classLabel=[]
    index=0
    for line in lines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabel.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabel

def show(datingDataMat,datingLabels):
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15 * np.array(datingLabels), 15 * np.array(datingLabels))
    plt.show()

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges=maxVals-minVals
    row=dataSet.shape[0]
    normDataSet=dataSet-np.tile(minVals,[row,1])
    normDataSet=normDataSet/np.tile(ranges,[row,1])
    return normDataSet,ranges,minVals

def datingClassTest(filename):
    datingDataMat, datingLabels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    testRatio=0.1
    row=normMat.shape[0]
    numTest =int(testRatio * row)
    errorCount=0.0
    for i in range(numTest):
        classType=classify0(normMat[i,:],normMat[numTest:row,:],datingLabels[numTest:row],3)
        print("the classfier came back with %d,the real answer is %d"%(classType,datingLabels[i]))
        if (classType!=datingLabels[i]):errorCount+=1
    print("the total error rate is:%f"%(errorCount/float(numTest)))

def classifyPerson(filename):
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(input("percentage of time spent playing video games?"))
    ffMiles=float(input("frequent flier miles earned per year?"))
    iceCream=float(input("liters of ice ceram consumed per year?"))
    datingDataMat, datingLabels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    classType = classify0(([ffMiles,percentTats,iceCream]-minVals)/ranges, normMat, datingLabels, 3)

    print("You will probably like this person:%s"%(resultList[classType-1]))

if __name__ == '__main__':
    group,labels=createDataSet()
    filename='/home/jgz/下载/machinelearninginaction/Ch02/datingTestSet2.txt'
    # datingClassTest(filename)
    classifyPerson(filename)
