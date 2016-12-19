# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 18:57:01 2016

@author: Harikrishnan
"""

from nltk.book import *
text2



#text5 is a chat corpus

#concordance will just display the occurrence of each word with context
text5.concordance("cycle")
text6.concordance("going")
text5.concordance("rofl")
text5.similar("rofl")
text4.concordance("cycle")

text1.concordance("love")

#similar will give us the what other word appear in the same context
text1.similar("love")
text2.similar("monstrous")

#Common context will give the context that are shared by botth the word
text2.common_contexts(["monstrous","very"])

#determines the locatio of the word from the starting poistion.
text4.dispersion_plot(["citizens","democracy","freedom","duties","America","cycle"])

text4.generate()

#The below will count all the words,Punctuations
len(text3)
#It will give count of uniques set of words in a  sorted order
len(sorted(set(text3)))
#It gives the average number of times a word is repeated
len(text3)/len(set(text3))




text4.count("a")
len(text4)
100 * text4.count("a") / float(len(text4))
ans

sent1

saying  = ['After','all','is','said','and','done','more','is','said','than','done','done']
tokens = set(saying)
tokens = sorted(tokens)
tokens[:2]


#To find the most frequent words

fdist1 = FreqDist(text1)
fdist1
VOCUBULARY = fdist1.keys()
VOCUBULARY[1:50]
#frequency distribution for a particular word
fdist1['whale']

fdist1.plot(50,cumulative = False)
fdist1.plot(50,cumulative = True)

#shos the list of words that occurs only once
fdist1.hapaxes()

#the below function will find the words that are having more then the number of mentioned characters
def findlongWord(text,howLong):
    v=set(text)
    long_words = [w for w in v if len(w) > howLong]
    sorted(long_words)
    print long_words
    
findlongWord(text1,19)    

##Find the collocation in teh sentence text4.
text4.collocations()

#To count the frequency distribution of words having different word length.
fdist = FreqDist([len(w) for w in text1])

fdist
fdist.keys()  #return the key
fdist.items() #return each element with their count
fdist.max() #find the element which is having maximum number of counts
fdist.freq(3)



h = ['Monty','Python']*2
h