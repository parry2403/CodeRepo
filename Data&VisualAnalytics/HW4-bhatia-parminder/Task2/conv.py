__author__ = 'Parry'

import os
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.tag.stanford import POSTagger
from nltk.parse.stanford import StanfordParser


mys = "pos"  + ".csv"
pos = open(mys,"w")

f = open('hw4-task1-data.tsv','r')
data = f.read().splitlines()
for line in data:
    wordb = line.rsplit('\t')
    pos.write(str(wordb[0]))
    i =1
    for wrd in wordb:

         pos.write(str(wrd))
         if i!=len(wordb):
             pos.write(",")
         i=i+1
    pos.write("\n")


