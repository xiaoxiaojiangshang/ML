
import numpy as np
from os import listdir
from KNN import classify0

def img2vector(filename):
    returnVect=np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

def handWritingClassTest(filenameTraining,filenameTest):
    hwLabels=[]
    trainingFileList=listdir(filenameTraining)
    mTrain=len(trainingFileList)
    trainingMat=np.zeros((mTrain,1024))
    for i in range(mTrain):
        label=trainingFileList[i][0]
        hwLabels.append(int(label))
        compPath=filenameTraining+"/"+trainingFileList[i]
        trainingMat[i,:]=img2vector(compPath)

    trainingFileList = listdir(filenameTest)
    mTest = len(filenameTest)
    errorCount=0
    for i in range(mTest):
        label = int(trainingFileList[i][0])
        compPathTest = filenameTraining + "/" + trainingFileList[i]
        vecorUnderTest=img2vector(compPathTest)
        classfierResult=classify0(vecorUnderTest,trainingMat,hwLabels,3)
        print("the classfier came back with %d,the real answer is : %d"%(classfierResult,label))
        if(classfierResult!=label):
            errorCount+=1
    print("the total number of erros is %d"%(errorCount))
    print("the total error rate is :%f"%(errorCount/float(mTest)))


if __name__=='__main__':
    filenameTest="/home/jgz/下载/machinelearninginaction/Ch02/testDigits"
    filenameTraining="/home/jgz/下载/machinelearninginaction/Ch02/trainingDigits"
    handWritingClassTest(filenameTraining, filenameTest)