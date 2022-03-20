from numpy import  *
import operator
import numpy as np



def CreateSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','B','B','B']
    return group,labels

def classify0(inX,dataset,labels,k):
    datasize=dataset.shape[0]
    print((inX))
    diffmat=tile(inX,(datasize,1))-dataset
    sqdiffmat=diffmat**2
    print(sqdiffmat)
    sqdistances=sqdiffmat.sum(axis=1)
    print(sqdistances)
    distances=sqdistances**0.5
    sortindex=distances.argsort()
    classcount={}
    for i in range(k):
        votelabel=labels[sortindex[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+1
    print(classcount)
    sortclasscount=sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    print(sortclasscount[0][0])

group,labels=CreateSet()
classify0([0,0],group,labels,3)