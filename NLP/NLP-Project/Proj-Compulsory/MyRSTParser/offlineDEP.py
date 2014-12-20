__author__ = 'Parry'

import os
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.tag.stanford import POSTagger
from nltk.parse.stanford import StanfordParser
from collections import deque
def _parse_output(output_,edus,dep):
        res = []
        cur_lines = []
     #   print output_
        wrdroot = {}
        curr = edus.popleft()
        chk = word_tokenize(curr)
        depsEDU = []
      #  print curr
        for line in output_.splitlines(False):
            if line == '':
            #    res.append(Tree.fromstring('\n'.join(cur_lines)))
                cur_lines = []
            else:
                  root =line.split('(')
                #print root[1].split(',')[1].split('-')[0].strip()
                #print root[1].split(',')[0].split('-')[0].strip()
              #    print root
                  if root !='':
                     word = root[1].split(',')[1].split('-')[0].strip()
                     wordRoot= root[1].split(',')[0].split('-')[0].strip()
                  #   print word
                  #   print curr
                 #    print edus
                     if word not in curr:
                     #    print'Split*****',word
                     #    print depsEDU
                         dep.write(str(curr.strip()))
                         dep.write("@#%^&*")
                         for wrds in depsEDU:
                            dep.write(str(wrds))
                            dep.write("\t")
                         dep.write("\n")
                         depsEDU =[]
                         if len(edus)==0:
                             break
                         curr = edus.popleft()
                         chk = word_tokenize(curr)
                     if wordRoot == 'ROOT':
                          depsEDU.append((str(word),str(wordRoot),"R"))
                     elif wordRoot not in curr:
                      #   print word
                         #  if (str(word),"U") not in depsEDU:
                         try:
                                if str(word) not in depsEDU:
                                      depsEDU.append((str(word),str(wordRoot),"U"))
                         except Exception :
                          #  print edus
                            print 's'
                          #    print depsEDU

        dep.write(str(curr.strip()))
        dep.write("@#%^&*")
        for wrds in depsEDU:
                dep.write(str(wrds))
                dep.write("\t")
        dep.write("\n")
        depsEDU =[]
        return wrdroot

#mys1 = "dpossall"  + ".txt"
#dep = open(mys1,"w")
english_postagger = POSTagger('../postagger/models/english-bidirectional-distsim.tagger', '../postagger/stanford-postagger.jar')
english_parser = StanfordParser('../postagger/stanford-parser.jar', '../parser/stanford-parser-3.5.0-models.jar')

i=0
for fname in os.listdir('test_data'):

     if fname.endswith('.edus') :
            print i
            print fname
            i=i+1
            if True:
                f = open(os.path.join('test_data',fname),'r')
                mys1 =os.path.join('test_data', fname.split(".")[0] +".dep")
                print mys1
                dep = open(mys1,"w")
                data = f.read().splitlines()
                edus = deque()

                sentence = None
                for line in data:
                       words = word_tokenize(line)
                       if sentence is None:
                            sentence = line.strip()
                        #    print sentence
                       else:
                           sentence = sentence + " " + line.strip()
                       l= words[-1]
                     #  print 'awesome' in 'wheather is awesome here dude'
                    #   print l

                       edus.append(line.strip())
                    #   print line.strip()
                      # print ".\""
                   #    print line.strip()[-2:]
                       if line.strip()[-1]=="." or line.strip()[-2:]==".\"":
                         #  print sentence
                        #   print edus
                           rootWord = _parse_output(english_parser.raw_parse(sentence),edus,dep)
                       #    print 'end'
                           sentence =None
                           edus = deque()
                     #  for sentence in sentences:
                      #    rootWord = _parse_output(english_parser.raw_parse(sentence))
                     #     dep.write(str(sentence).split())
                      #    dep.write("@#%^&*")
                      #    dep.write(str(rootWord))
                      #    dep.write("\n")
                      #    print i
                      #    i=i+1
                if sentence!=None:
                     rootWord = _parse_output(english_parser.raw_parse(sentence),edus,dep)
                       #    print 'end'
                     sentence =None
                     edus = deque()


