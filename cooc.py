# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:24:32 2017

@author: SANDIPAN
"""

from last300317 import dwords,docwords,totaldocs,allwordscount,wordfreqlist
import numpy as np



matrix=[]
coprob=[]
problist=[]
condprob=[]
matrix=np.zeros((len(dwords),len(dwords)),dtype=np.int)
condprob=np.zeros((len(dwords),len(dwords)),dtype=np.float)

def cooc(fnum):
#    for word1 in dwords:
#        for word2 in docwords[fnum]:
#            if word1!=word2:
#                print word1,word2
#                matrix[dwords.index(word1)][dwords.index(word2)]+=1
     for i in range(0,len(docwords[fnum])):
         ind=i
         if (ind+1)< len(docwords[fnum]):
             word=docwords[fnum][ind]
             nextword=docwords[fnum][ind+1]
             if word!=nextword:
              matrix[dwords.index(word)][dwords.index(nextword)]+=1
              matrix[dwords.index(nextword)][dwords.index(word)]+=1
        
                       
for i in range(0,totaldocs):
    cooc(i)
    
coprob=[x/(float)(allwordscount-1) for x in matrix]

for k in range(0,len(wordfreqlist)):
    p=wordfreqlist[k][1]/(float)(allwordscount)
    problist.append((wordfreqlist[k][0],p))
    
for j in range(0,len(problist)):
    for k in range(0,len(problist)):
        p=coprob[j][k]/(float)(problist[k][1])
        condprob[j][k]=p
        if condprob[j][k]>1:
            condprob[j][k]=1

#np.save("conditionalprob_matrix_t", condprob, allow_pickle=True, fix_imports=True)
#np.save("dwords_t", dwords, allow_pickle=True, fix_imports=True)

