# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:23:08 2017

@author: Punyajoy Saha
"""

import nltk
import math
from os import system
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
corpus_path='C:/Users/Punyajoy Saha/Desktop/corpus/c '

          
          
#def filtered(filename):
##  filename=raw_input('Enter the filename: ')
#  doc=open(filename,'r')
#  str1 =doc.read()
#  str1=str1.decode('ascii','ignore')         #the whole document is read in one string 
#  tokens=nltk.word_tokenize(str1); 
#  token_new=[word for word in tokens if word not in stopwords.words('english')]
#  words=[word.lower() for word in token_new if word.isalpha()]
#  str1=""
#  for u in words:
#      str1=str1+" "+u
#  return str1        
#  
#  
#corpus=[]  
#for i in range(0,2364):
#     print(i)
#     str1=corpus_path+'('+str(i+1)+')'+'.txt'
#     word_vec=filtered(str1)
#     corpus.append(word_vec)
#
#vectorizer = TfidfVectorizer(min_df=1)
#X = vectorizer.fit_transform(corpus)
#idf = vectorizer._tfidf.idf_
#idf_1=sorted(idf)
#print dict(zip(vectorizer.get_feature_names(), idf_1))
#

"""use the X created in KNN+tfidf method"""

"""this step will take some time"""
#for i in range(0,2365):
#    for j in range(0,27528):
#        if X[i,j]>0:
#            X[i,j]=1
#            print i
#        print j    
        
Y=np.zeros((2364,1),dtype='int32')

for i in range(0,291):
    Y[i,0]=1
for i in range(291,561):
    Y[i,0]=2
for i in range(561,1061):
    Y[i,0]=3
for i in range(1061,1341):
    Y[i,0]=4
for i in range(1341,1698):
    Y[i,0]=5
for i in range(1698,1824):
    Y[i,0]=1
for i in range(1824,1940):
    Y[i,0]=2
for i in range(1940,2090):
    Y[i,0]=3
for i in range(2090,2211):
    Y[i,0]=4
for i in range(2211,2364):
    Y[i,0]=5


#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X[0:1697,:], Y[0:1697,:])
#

neigh = KNeighborsClassifier(n_neighbors=3)
Y=np.ravel(Y)
neigh.fit(X, Y)
Y_predict=neigh.predict(X[1:,:]) 
k=0;
success=np.zeros((5,2),dtype='int32')

count=0
for i in range(1698,1824):
    if(Y[i]==Y_predict[k]):
        success[0,0]=success[0,0]+1
    k=k+1
    count=count+1
success[0,1]=count    
count=0
for i in range(1824,1940):
    if(Y[i]==Y_predict[k]):
        success[1,0]=success[1,0]+1
    k=k+1
    count=count+1
success[1,1]=count
count=0
for i in range(1940,2090):
    if(Y[i]==Y_predict[k]):
        success[2,0]=success[2,0]+1
    k=k+1
    count=count+1
success[2,1]=count
count=0    
for i in range(2090,2211):
    if(Y[i]==Y_predict[k]):
        success[3,0]=success[3,0]+1
    k=k+1
    count=count+1
success[3,1]=count
count=0    
for i in range(2211,2363):
    if(Y[i]==Y_predict[k]):
        success[4,0]=success[4,0]+1
    k=k+1
    count=count+1
success[4,1]=count    
count=0



""" divide success[i]/count[i]  to get success percentage"""

tree.export_graphviz(clf, out_file='tree.dot') #produces dot file

