import nltk
import math
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
corpus_path='C:/Users/Punyajoy Saha/Desktop/corpus/c '

          
          
def filtered(filename):
#  filename=raw_input('Enter the filename: ')
  doc=open(filename,'r')
  str1 =doc.read()
  str1=str1.decode('ascii','ignore')         #the whole document is read in one string 
  tokens=nltk.word_tokenize(str1); 
  token_new=[word for word in tokens if word not in stopwords.words('english')]
  words=[word.lower() for word in token_new if word.isalpha()]
  str1=""
  for u in words:
      str1=str1+" "+u
  return str1        
  
  
corpus=[]  
for i in range(0,2364):
     print(i)
     str1=corpus_path+'('+str(i+1)+')'+'.txt'
     word_vec=filtered(str1)
     corpus.append(word_vec)

vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer._tfidf.idf_
idf_1=sorted(idf)
print dict(zip(vectorizer.get_feature_names(), idf_1))


#dist=[(0,[(0,0)])]
#count=0
#for v in range(1698,2366):
#    dist.append((v,[]))
#    for u in range(0,1698):
#        dista=0;
#        for w in range(0,27528):
#            dista=dista+pow((X[v,w]-X[u,w]),2)
#        dista=math.sqrt(dista)
#        dist[count][1].append((u ,dista))
#        print u
#    count =count+1
#        
#    
#
#





