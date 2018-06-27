
import nltk as nlp
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import inflection

#from pattern.text.en import singularize

#the variables that should be known
#listsen is the no of basic sentences included in the first chance



ps = PorterStemmer()
empty=[]
listsen=[]
list1=[("9999",[(1)],[("prev","ppos","line","npos","next")])]
imp_words=[]
class_basic=[]       
count_1=[0,0,0,0,0]      
basic_pred=[]
index_my=[]   
filter_tag=[]
sen_in_forest=[[],[],[],[],[]]
list_of_all=[[],[],[],[],[]]
list_sen_all=[[],[],[],[],[]]
list_percentage=[]
    
#FUNCTION DEFINED    

#column defined#
def column(matrix,i):
    return [row[i] for row in matrix]
def column_res(matrix,i,j):
    for r in range(0,j):
        return [row[i] for row in matrix]
######preprocessing data in a text document########     
def filtered(filename):
#  filename=raw_input('Enter the filename: ')
  doc=open(filename,'r')
  str1 =doc.read()
  str1=str1.decode('ascii','ignore')         #the whole document is read in one string 
  tokens=word_tokenize(str1);   #chracters are converted into tokens 
  
  
  filter_tag1=nlp.pos_tag(tokens)
  for word in filter_tag1:
     word1=inflection.singularize(word[0])
     word1=word1.lower()
     filter_tag.append((word1,word[1]))
     #filter_tag.remove(word)        
  
  line=[]
  #now from words phrases are formed breaking at question mark,full stop, comma 
  for word in filter_tag:
       if(word[0] != "." and word[1] == 'NN'):     # here we are inserting each noun in different line 
          line.append(word[0])                                              # if word is not a full stop then we include it in a the line   
       if(word[0] == "."):
          listsen.append(line)                      #once we get the line we insert the line into list of sentences 
          line=[]   
  #extracting the nouns.....
  i=0
  count=0

  
           
  for line in listsen:          
       r=0                            #for each line 
       for word in line:           #for each word in the line 
              prev1="NULL"             #setting data to null 
              next1="NULL"
              ppos=-1
              npos=-1
              #column of the words included in the list
              word_col=column(list1,0)
                    
              # searching  for closest right and left child
              if(r>0):
                prev1=line[r-1]
                ppos=word_col.index(prev1)     
              # left child is assignd if  not found then NULL given to it              
             
              
              # searching for the right child 
              if(r<len(line)-1):                         
                  next1=line[r+1]                        # next word is the word to be inserted 
                  try:
                     test=word_col.index(next1)          # if the value is found in the existing list 
                  except ValueError:                   
                         try:
                          word_col.index(word)        #checking if the word that we considered is part 
                          
                         except ValueError:
                            npos=len(list1)+1           #if the word will be inserted for the first time then +1 other wise +2
                                         
                         else:
                            
                            npos=len(list1)
                  else:
                        npos=test                                                                     
                       
                        
                  
                  
                  
                      
              #forming the tuple with the above data
              tuple1=(prev1,ppos,count,npos,next1)
              listtemp=['9999']
              for j in range(1,i+1):
                 listtemp.append(list1[j][0])
                 
              if word not in listtemp:
                  
                  w=(word,[(1)],[tuple1])
                  list1.append(w)
                  i=i+1
              else:
                  m=listtemp.index(word)
                  list1[m][2].append(tuple1)
                  list1[m][1].append((1))
              r=r+1
       count+=1            
  #list1.sort(key=lambda x: x[1],reverse=True)
  
  # taking a word as important if its frequency is equal to 50% of the max frequency 
  #assuming each word has occured in each sentence only once
  return filter_tag
##### end of a function #####
suc=0
token_basic=[]
token_politics=[]
token_sport=[]
token_business=[]
token_entertain=[]
token_science=[]

list_basic=[[],[],[],[],[]]
list_basic_1=[[],[],[],[],[]]
list_basic_ini=[]
list_cp=[]
list_dwords=[]    
######INITALIZE THE BASIC THINGS##########
def initialize():
    fsports = open('basic_sports.txt','r')
    fpolitics = open('basic_politics.txt','r')
    fentertain = open('basic_entertainment.txt','r')
    fscience = open('basic_tech.txt','r')
    fbusiness = open('basic_business.txt','r') 

    #string reading 
    str1=fpolitics.read()
    class_basic.append("politics")
    str2=fentertain.read()
    class_basic.append("entertain")
    str3=fsports.read()
    class_basic.append("sports")
    str4=fscience.read()
    class_basic.append("tech")
    str5=fbusiness.read()
    class_basic.append("business")
    
    #combining into one string 
    str_basic=str1+str2+str3+str4+str5
    token=word_tokenize(str_basic)
    countin=0
    for word in token:
        token_basic.append(word)
        if(countin/5==0):
            token_politics.append((word,1))
        if(countin/5==1):
            token_entertain.append((word,1))
        if(countin/5==2):
            token_sport.append((word,1))
        if(countin/5==3):
            token_science.append((word,1))
        if(countin/5==4):
            token_business.append((word,1))
        countin=countin+1
    
    list_cp.append(conditionalprob_matrix_p)
    list_cp.append(conditionalprob_matrix_e)
    list_cp.append(conditionalprob_matrix_s)
    list_cp.append(conditionalprob_matrix_t)
    list_cp.append(conditionalprob_matrix_b)
      
    list_dwords.append(dwords_p.tolist())
    list_dwords.append(dwords_e.tolist())
    list_dwords.append(dwords_s.tolist())
    list_dwords.append(dwords_t.tolist())
    list_dwords.append(dwords_b.tolist())

    list_basic_ini.append(token_politics)
    list_basic_ini.append(token_entertain)
    list_basic_ini.append(token_sport)
    list_basic_ini.append(token_science)
    list_basic_ini.append(token_business)
    
   






##### MAIN ALGORITHM ####### 
def percentage_sen():
    
    
    #finding basic words in documents
    for w in imp_words:
        for i in range(0,5):
         if w[0] in column(list_basic[i],0):
            ind_basic=column(list_basic[i],0).index(w[0])
            ind=list1.index(w)
            index_my.append((ind,ind_basic))
            count_1[i]+=1
            
#    if(len(index)==0):
#      exit(0)
#    
    j=0      
    for i in count_1:
        if i>0:
           basic_pred.append((j,i)) 
        j=j+1

     
######end of basic sentence finding######

list_al=[]
leng=0
A=0.053
B=2.403
def relation_coeff(dist,freq):
    h=A*dist+B*freq
    return h

def new_basic_word(i,list_imp,k,list_all_words,all_sen,word_count):
    sen=[]
    list_word=[]
    index_class=k[1]
    if i==0:
        for word in list_imp[2]:
            if word[0] in column_res(list_basic[index_class],0,5):
                index_basic=list_imp[2].index(word)
                base=column_res(list_basic[index_class],0,5)
                basic_index=base.index(word[0])
                rc=list_basic[index_class][basic_index][1]
                tuple_b=(word[0],index_basic,1,len(word[1])/word_count,rc)
                list_word.append((tuple_b))
                list_all_words.append((word[0],rc))
                for tuple_1 in word[2]:
                    if tuple_1[2] not in all_sen:
                        sen.append(tuple_1[2])
                        all_sen.append(tuple_1[2])
                        
    else:
        j=0
        for word_1 in list_basic_1[k[1]][i-1][1]:
           if j<5: 
             tuple_now=list_imp[2][word_1[1]]
             cop_index=list_dwords[k[1]].index(word_1[0])
             for word in tuple_now[2]:
                    prev=word[0]                      ##storing the prev next and position of these
                    prev_pos=word[1]
                    nxt=word[4]
                    next_pos=word[3]
                    if prev != 'NULL' and  prev not in column(list_all_words,0):
                          try:
                                prev_index=list_dwords[k[1]].index(prev) 
                          except ValueError:
                                dist=0
                          else:
                                dist=list_cp[k[1]][cop_index][prev_index]
                                freq=len(list_imp[2][prev_pos][1])
                                rc=relation_coeff(dist,freq/float(word_count))
                                list_word.append((prev,prev_pos,dist,freq,rc))
                                list_all_words.append((prev,rc))
                                for tuple_1 in list_imp[2][prev_pos][2]:
                                    if tuple_1[2] not in all_sen:
                                          sen.append(tuple_1[2])
                                          all_sen.append(tuple_1[2])
                                       
                                                                                    
                 
                    
                    if nxt != 'NULL' and  nxt not in column(list_all_words,0):
                          try:
                                next_index=list_dwords[k[1]].index(nxt)
                          except ValueError:
                                dist=0
                          else:
                                dist=list_cp[k[1]][cop_index][next_index]
                                freq=len(list_imp[2][next_pos][1])
                                rc=relation_coeff(dist,freq/float(word_count))
                                list_word.append((nxt,next_pos,dist,freq,rc))
                                list_all_words.append((nxt,rc))
                                for tuple_1 in list_imp[2][next_pos][2]:
                                    if tuple_1[2] not in all_sen:
                                          sen.append(tuple_1[2])
                                          all_sen.append(tuple_1[2])
                                
                    
           j=j+1    
    list_word.sort(key=lambda x: x[4],reverse=True)
    return [list_word,sen]    
    
    
    
def graph_classification(leng):
    word_count=0
    list_cur=[]           
    if len(suc)>leng:
        leng=len(suc)                         #length of the success is inc hence the leng is changed 
        index=int(suc[leng-1][0])             #index of the doc to be analyzed        
        list_imp=list_all[index-1]
        for i in list_all[index-1][1]:
            word_count=word_count+len(i)
 
        for i in range(0,5):
            list_cur.append((list_all[index-1][5][i],i))
        list_cur.sort(key=lambda x: x[0],reverse=True)   ### sorting to fix the classification order
        for k in list_cur:
            if k[0]>0:
                list_all_words=[]
                all_sen=[]
                i=0
                [list_word,sen]=new_basic_word(i,list_imp,k,list_all_words,all_sen,word_count)
                list_basic_1[k[1]].append((i,list_word))
                sen_in_forest[k[1]].append((i,sen))
                i=i+1
                while len(list_basic_1[k[1]][i-1][1]) != 0:
                    [list_word,sen]=new_basic_word(i,list_imp,k,list_all_words,all_sen,word_count)
                    list_basic_1[k[1]].append((i,list_word))
                    sen_in_forest[k[1]].append((i,sen))
                    i=i+1
                list_all_words.sort(key=lambda x: x[1],reverse=True)
                list_of_all[k[1]].append(list_all_words)
                list_sen_all[k[1]].append(all_sen)
                list_percentage.append((k[1],len(all_sen)*100/float(len(list_imp[1]))))
                list_percentage.sort(key=lambda x: x[1],reverse=True)
               
                    
            else:
                break
    return leng          
   
######## end of function #######    
list_all=[]      
suc=[]
len1=[]
listq=[]
finallist_all=[]
filepath1='E:/computerscience/my projects/text_analytics/text_analytics/entertainment/e_test/e '
filepath2='E:/computerscience/my projects/text_analytics/text_analytics/allsports/s_test/s '
filepath3='E:/computerscience/my projects/text_analytics/text_analytics/politics/p_test/p '
filepath4='E:/computerscience/my projects/text_analytics/text_analytics/business/b_test/b '
filepath5='E:/computerscience/my projects/text_analytics/text_analytics/tech/t_test/t '




filepath=[(filepath3,126),(filepath1,117),(filepath2,151),(filepath5,121),(filepath4,153)]


initialize()




total=[]
co=0
for file_1 in filepath:
    empty=[]
    success=0
    failure=0
    failure_class=[0,0,0,0,0]
    ambiguity=0
    relation=[0,0,0,0,0]
    sentence_percentage=0
    avg=0
    listsen=[]
    list1=[("9999",[(1)],[("prev","ppos","line","npos","next")])]
    imp_words=[]
    class_basic=[]       
    count_1=[0,0,0,0,0]      
    basic_pred=[]
    index_my=[]     
    filter_tag=[]
    sen_in_forest=[[],[],[],[],[]]
    list_of_all=[[],[],[],[],[]]
    list_sen_all=[[],[],[],[],[]]
    list_percentage=[]

    finallist_all=[]
    list_all=[]
    suc=[]
    len1=[]
    listq=[]
    list_basic=[[],[],[],[],[]]
    list_basic_1=[[],[],[],[],[]]
    list_al=[]
    leng=0
    list_all=[]      
    suc=[]
    len1=[]
    listq=[]
    finallist_all=[]
 

    for i in range(1,file_1[1]):
     #all the values are again initialised again.    
     listsen=[]
     list1=[("9999",[(1)],[("prev","npos","line","ppos","next")])]
     imp_words=[]       
     count_1=[0,0,0,0,0]      
     basic_pred=[]
     index_my=[]   
     sen_in_forest=[[],[],[],[],[]]
     len1=[]
     basic_word_used=[]
     filter_tag=[]
     filter_tag1=[]
     list_basic_1=[[],[],[],[],[]]
     list_basic=[[],[],[],[],[]]
     list_of_all=[[],[],[],[],[]]
     list_sen_all=[[],[],[],[],[]]
     list_percentage=[]
     
     print(i)
     str1=file_1[0]+'('+str(i)+')'+'.txt'
     filtered(str1)
     len_col=column(list1,1)
     for wrd in len_col:
         len1.append(len(wrd))
       
     freq_threshold=(10*max(len1)/100)
     if freq_threshold<2:
          freq_threshold=2
     for word in list1:
          if len(word[1]) >= freq_threshold:
             imp_words.append(word)
     flag=0
     list_all.append((i,listsen,list1,imp_words,class_basic,count_1,basic_pred,index_my))
         
     for j in range(0,5):
         list_basic[0].append(token_politics[j])
         list_basic[1].append(token_entertain[j])
         list_basic[2].append(token_sport[j])
         list_basic[3].append(token_science[j])
         list_basic[4].append(token_business[j])
         
     str_basic=percentage_sen()
     if(len(basic_pred)>0):
        suc.append((i,basic_pred))
     basic_word_used.append(list_basic)
         
     leng=graph_classification(leng)
     if len(list_percentage)>0:
         list_ap=list_of_all[list_percentage[0][0]][0] 
         cou=0
              
         if len(list_percentage)==1:
             if list_percentage[0][0]==(co) and list_percentage[0][1] > 0:
                 success=success+1
                 avg+=list_percentage[0][1]
                 for g in range(0,len(list_ap)):
                  if  list_ap[g][0] not in column(list_basic_ini[list_percentage[0][0]],0):
                     list_basic_ini[list_percentage[0][0]].append(list_ap[g])
                     cou=cou+1
                     if cou==5:
                         break
                  else:
                     list_ba=column(list_basic_ini[list_percentage[0][0]],0)
                     h=list_ba.index(list_ap[g][0])
                     if(list_basic_ini[list_percentage[0][0]][h][1]!=1):
                       rc_avg=(list_basic_ini[list_percentage[0][0]][h][1]+list_ap[g][1])/2
                       list_basic_ini[list_percentage[0][0]].remove(list_basic_ini[list_percentage[0][0]][h])               
                       list_basic_ini[list_percentage[0][0]].append((list_ap[g][0],rc_avg))
                 list_basic_ini[list_percentage[0][0]].sort(key=lambda x: x[1],reverse=True)



             else:
                 failure=failure+1
                 if list_percentage[0][1]>0:
                     failure_class[list_percentage[0][0]]+=1
         else:
              count_am=column(list_percentage,1).count(list_percentage[0][1])
              
              if count_am == 1:
                  if list_percentage[0][0]==(co) and list_percentage[0][1]>0:
                      success=success+1
                      avg+=list_percentage[0][1]
                      for g in range(0,len(list_ap)):
                          if  list_ap[g][0] not in column(list_basic_ini[list_percentage[0][0]],0):
                             list_basic_ini[list_percentage[0][0]].append(list_ap[g])
                             cou=cou+1
                             if cou==5:
                                 break
                          else:
                             list_ba=column(list_basic_ini[list_percentage[0][0]],0)
                             h=list_ba.index(list_ap[g][0])
                             if(list_basic_ini[list_percentage[0][0]][h][1]!=1):
                                 rc_avg=(list_basic_ini[list_percentage[0][0]][h][1]+list_ap[g][1])/2
                                 list_basic_ini[list_percentage[0][0]].remove(list_basic_ini[list_percentage[0][0]][h])               
                                 list_basic_ini[list_percentage[0][0]].append((list_ap[g][0],rc_avg))
                      list_basic_ini[list_percentage[0][0]].sort(key=lambda x: x[1],reverse=True)
                  else:
                      failure=failure+1
                      if list_percentage[0][1]>0:
                          failure_class[list_percentage[0][0]]+=1
              else:
                  ambiguity+=1
                  if co in column_res(list_percentage,0,count_am-1): 
                     for l in range(0,count_am):
                         relation[list_percentage[l][0]]+=1
                      
                      
                               
     finallist_all.append((i,listsen,list1,imp_words,class_basic,count_1,basic_pred,index_my,sen_in_forest,list_basic_1,list_of_all,list_sen_all,list_percentage,basic_word_used))
      
             
      
     
    co=co+1 
    total.append((finallist_all,suc,(success*100/float(len(finallist_all))),((failure+(len(finallist_all)-len(suc)))*100/float(len(finallist_all))),(ambiguity*100/float(len(finallist_all))),relation,avg/float(success),failure_class))
     
             
             
             
      
     
     
    

    