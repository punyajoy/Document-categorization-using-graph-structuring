
"""
Created on Sun Feb 05 12:43:40 2017

@author: SANDIPAN
"""
#!/usr/bin/python
# encoding=utf8
flag=1
start1=0
start2=0

def column(matrix,i):
    return [row[i] for row in matrix]

import nltk as nlp
from nltk.tokenize import word_tokenize
import math
import inflection
#from nltk.stem import PorterStemmer


#ps = PorterStemmer()
#from nltk.corpus import stopwords
#from collections import Counter 

allwordscount=0
wts=[]
wordfreqlist=[]
wordcount=[]
counts=[]
dwords=[]
docwords=[]
listtf=[]
listidf=[]
docsappeared=[]
weights=[]
finallist=[]
stoplist=[',','<','>','?','/','"',':',';','[','{','}',']','|','\'','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=']
def filtered(filename):
    #filename=raw_input('Enter the filename: ')
    doc=open(filename,'r')
    
    str2 =doc.read()  
    str2=str2.decode('ascii','ignore')   
    tokens=word_tokenize(str2)
    
    #filtered_list=[]
#    stop_words = stopwords.words('english')
#    p_list=['.','!','(',')',',','"','\'','?',':',';']
#    avoid_words=stop_words+p_list        
#    for w in tokens:
#       w=w.lower()
#       if w not in avoid_words:
#          filtered_list.append(w)
    j=0      
    reqd_tags=['NN','NNS']
    filter_tag=nlp.pos_tag(tokens)
    filter_new=[]
    
    for w in filter_tag:
       if filter_tag[j][1] in reqd_tags:
          w1=w[0].lower()
          filter_new.append((w1,w[1]))
       j=j+1
    listw=[]  
    i=0         
    for word in filter_new:
        w=inflection.singularize(filter_new[i][0])
        listw.append(w) 
        
        i=i+1       

    docwords.append(listw)
    
    i=0
    noofwords=0
    tf=0
    dcount=0
    for word in listw:
       if word not in dwords:
            dwords.append(word)
            dcount=dcount+1
#           z=0
#           for word in column(docsappeared,0):
#               if word==docsappeared[z][0] and visited[z][1]!=1 and idf==0:
#                  x=docsappeared[z][1]+1
#                  docsappeared.remove(docsappeared[z])
#                  docsappeared.append((word,x))
#                  visited.remove(visited[z])
#                  visited.append((word,0))
#           z=z+1
#           for j in range(0,i):
#               if word==dwords[j]:
#                   wordcount[j]+=1
#                   break
       noofwords=noofwords+1
     
       
    global start1    
    start1=start1+dcount
    for k in range((start1-dcount),len(dwords)):
        counts.append(0)
        wordcount.append(0)
        
    for word in dwords:
        c=listw.count(word)
        wordcount[dwords.index(word)]+=c
                  
    for word in dwords:
        if listw.count(word)>0:
            counts[dwords.index(word)]+=1
    
    list1=[]
    for word,count in zip(dwords,wordcount):
        if word not in column(list1,0):
           list1.append((word,count))     
#    global start1    
#    start1=start1+dcount
#    newdwords=[]
#    for k in range((start1-dcount),len(dwords)):
#        newdwords.append(dwords[k])
#      
#    list3=[]
#    for word in newdwords:
#           list3.append((word,listw.count(word)))  
#    
#    for word in newdwords:
#           flag=0
#           for z in range(0,len(docsappeared)):
#               if word==docsappeared[z][0]:
#                  for y in range(0,len(list3)):
#                      if list3[y][0]==docsappeared[z][0] and list3[y][1]>0:
#                          x=docsappeared[z][1]+1
#                          list3.remove(list3[y])
#                          list3.append((word,-1))
#                          docsappeared.remove(docsappeared[z])
#                          docsappeared.append((word,x))
#                          flag=1
#                          break
#                  if flag==1:
#                     break
#               z=z+1
#           if flag==0:
#               docsappeared.append((word,1))
    
    global start2
    start2=start2+dcount
    
    for k in range((start2-dcount),len(list1)):
        tf=list1[k][1]/float(noofwords)
        listtf.append((list1[k][0],tf))   
    
     
    return list1
   
  
#    
#articles=['athletics/','cricket/','rugby/','tennis/']
#for a in articles:

    
filepath1='tech/'
totaldocs=100
for i in range(1,totaldocs+1):
     i='{:03d}'.format(i)
     print(i)
     str1=filepath1+str(i)+'.txt'
     list1=filtered(str1)  

#wordcount.sort(reverse=True)
for i in range(0,len(dwords)):
    wordfreqlist.append((dwords[i],wordcount[i]))
    
allwordscount=sum(wordcount)

for i in range(0,len(dwords)):
    docsappeared.append((dwords[i],counts[i]))
    
#x=math.log(num)
for k in range(0,len(docsappeared)):
    idf=math.log(totaldocs*float(docsappeared[k][1]))  #changing idf formula
    listidf.append((docsappeared[k][0],idf))
    
for k in range(0,len(docsappeared)):
#    weight=listtf[k][1]*listidf[k][1]
    weight=counts[k]*wordcount[k]
    finallist.append((docsappeared[k][0],weight))
    weights.append(weight)
for w in weights:
    wts.append(w)
weights.sort(reverse=True)
   
bvb=open("basic_tech.txt","w")
lastwt=0
for i in range(0,5):
       for x in range(lastwt,len(weights)):
           w=weights[lastwt]
           indw=wts.index(w)
           if finallist[indw][0] not in stoplist:
              bvb.write(finallist[indw][0])
              bvb.write("\n") 
              lastwt+=1
              break
           else:
               lastwt=+1
#      y=i
#      for x in weights:
#          if weights[y]==finallist[j][1]:
#              if finallist[j][0] not in stoplist:
#                bvb.write(finallist[j][0])
#                bvb.write("\n")
#                finallist.remove(finallist[j])
#                break
#              else:
#                  y=y+1
#                  j=0
#          else:
#              j=j+1
      
bvb.close()  


#del dwords[:]
#del wordcount[:]
#
#filepath2='sport/'
#for i in range(1,100):
#     i='{:03d}'.format(i)
#     print(i)
#     str1=filepath2+str(i)+'.txt'
#     list1=filtered(str1)       
#bvs=open("basic_sport.txt","w")
#for i in range(0,3):
#      j=0
#      y=i
#      for x in wordcount:
#          if wordcount[y]==list1[j][1]:
#              if list1[j][0] not in stoplist:
#                bvs.write(list1[j][0])
#                bvs.write("\n")
#                list1.remove(list1[j])
#                break
#              else:
#                  y=y+1
#                  j=0
#          else:
#              j=j+1
#bvs.close()
#
#del dwords[:]
#del wordcount[:]
#
#filepath3='entertainment/'
#for i in range(1,100):
#     i='{:03d}'.format(i)
#     print(i)
#     str1=filepath3+str(i)+'.txt'
#     list1=filtered(str1)       
#bve=open("basic_entertainment.txt","w")
#for i in range(0,3):
#      j=0
#      y=i
#      for x in wordcount:
#          if wordcount[y]==list1[j][1]:
#              if list1[j][0] not in stoplist:
#                bve.write(list1[j][0])
#                bve.write("\n")
#                list1.remove(list1[j])
#                break
#              else:
#                  y=y+1
#                  j=0
#          else:
#              j=j+1
#bve.close()          
#
#del dwords[:]
#del wordcount[:]
#
#filepath4='politics/'
#for i in range(1,100):
#     i='{:03d}'.format(i)
#     print(i)
#     str1=filepath4+str(i)+'.txt'
#     list1=filtered(str1)       
#bvp=open("basic_politics.txt","w")
#for i in range(0,3):
#      j=0
#      y=i
#      for x in wordcount:
#          if wordcount[y]==list1[j][1]:
#              if list1[j][0] not in stoplist:
#                bvp.write(list1[j][0])
#                bvp.write("\n")
#                list1.remove(list1[j])
#                break
#              else:
#                  y=y+1
#                  j=0
#          else:
#              j=j+1
#bvp.close()  
#
#del dwords[:]
#del wordcount[:]
#
#filepath5='tech/'
#for i in range(1,100):
#     i='{:03d}'.format(i)
#     print(i)
#     str1=filepath5+str(i)+'.txt'
#     list1=filtered(str1)       
#bvt=open("basic_tech.txt","w")
#for i in range(0,3):
#      j=0
#      y=i
#      for x in wordcount:
#          if wordcount[y]==list1[j][1]:
#              if list1[j][0] not in stoplist:
#                bvt.write(list1[j][0])
#                bvt.write("\n")
#                list1.remove(list1[j])
#                break
#              else:
#                  y=y+1
#                  j=0
#          else:
#              j=j+1
#bvt.close()  
#
#
#
#
#
#
#
##bv=open("basic_vocabulary.txt","w")
##for i in range(0,3):
##       j=0
##       for x in wordcount:
##           if wordcount[i]==list1[j][1]:
##               bv.write(list1[j][0])
##               bv.write("\n")
##               list1.remove(list1[j])
##               break
##           else:
##               j=j+1
##bv.close()              
