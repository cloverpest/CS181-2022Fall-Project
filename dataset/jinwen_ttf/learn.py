import numpy as np
import operator
from PIL import Image
from os import listdir
import skimage.io as io

def img2vector(filename):
    img_io = io.imread(filename)
    returnVect = img_io.reshape(1,2500)
    return returnVect

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def handwriteclasstest():
    hwLabels = []
    m = -1
    trainingFileList = listdir('standardlized')
    samples = sum([len(listdir('standardlized/' + cluster)) for cluster in trainingFileList])
    trainingMat = np.zeros((samples,2500))
    for cluster in trainingFileList:
        for f in listdir('standardlized/' + cluster):
            m += 1
            hwLabels.append(cluster)
            trainingMat[m,:] = img2vector('standardlized/' + cluster + '/' + f)
    
    errorCount = 0.0
    mTest = 0
    for cluster in trainingFileList:
        for f in listdir('standardlized/' + cluster):
            mTest += 1
            vectorUnderTest = img2vector('standardlized/' + cluster + '/' + f)
            classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 11)
            print("the classifier came back with: %s, the real answer is: %s" % (classifierResult, cluster))
            if (classifierResult != cluster): 
                errorCount += 1.0
    print("\the total number of errors is: %d" % errorCount)
    print("\the total error rate is: %f" % (errorCount/float(mTest)))

handwriteclasstest()