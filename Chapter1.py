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

len(text3)/len(set(text3))

text4.count("a")
len(text4)
100 * text4.count("a") / float(len(text4))
ans

sent1

saying  = ['After','all','is','said','and','done','more','is','said','than','done']
tokens = set(saying)
tokens = sorted(saying)
tokens[-2:]


v=set(text1)
long_word = []
long_words = [w for w in v if len(w) > 15]
w
long_words
for w in v:
    if len(w) > 15:
        long_word.append(w)


h = ['Monty','Python']*2
h