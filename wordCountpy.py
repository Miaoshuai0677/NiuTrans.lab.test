# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:51:34 2017

@author: wiohenshuai
"""

import os
os.chdir('E:/Project/NiuTrans.lab.test/sample-data/test1/')
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
res={}
with open("chinese.token.tag",'r') as f:
    for i in f.readlines():
            tmp=i.split(' ')
            tmp=tmp[0:len(tmp)-1]
            #print(tmp)
            for word in tmp:
                if word not in res:  
                    res[word] = 0  
                res[word] += 1   
f.close()


newValue=[]
newRes={}
for key,value in res.items():  
    
    try:
        newKey=key.split('/')[0]
        val=key.split('/')[1]
    except Exception,e:  
        print Exception,":",e
    
    valAll=val+' '+str(value)
    newValue.append(valAll)

    newRes.setdefault(newKey,[]).append(newValue)
    newValue=[]
    
    
for key1,value1 in newRes.items():
    print("%s的词性有%s种，分别为：" %(key1,len(value1)))
    
    for lis in iter(value1):
        cixing=''.join(lis).split(' ')[0]
        num=''.join(lis).split(' ')[1]
       # num=int(num)
        print('%s:%s' %(cixing,num))  
    
