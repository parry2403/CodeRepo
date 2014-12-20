__author__ = 'Parry'

import os
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.tag.stanford import POSTagger
from nltk.parse.stanford import StanfordParser

def _parse_output(output_):
        res = []
        cur_lines = []
        for line in output_.splitlines(False):
            if line == '':
            #    res.append(Tree.fromstring('\n'.join(cur_lines)))
                cur_lines = []
            else:
                root =line.split('(')
                if root[0] =='root':
                    return root[1].split(',')[1].split('-')[0].strip()
        return cur_lines
mys = "sentencepos2all"  + ".txt"
#mys1 = "dep2"  + ".txt"
pos = open(mys,"w")
#dep = open(mys1,"w")
english_postagger = POSTagger('../postagger/models/english-bidirectional-distsim.tagger', '../postagger/stanford-postagger.jar')
english_parser = StanfordParser('../postagger/stanford-parser.jar', '../parser/stanford-parser-3.5.0-models.jar')
length = 0
i=0
for fname in os.listdir('test_data'):

                if fname.endswith('.edus'):
                            print i
                            print fname
                            i=i+1
                            f = open(os.path.join('test_data',fname),'r')
                            mys1 =os.path.join('test_data', fname.split(".")[0] +".pos")
                            print mys1
                            pos = open(mys1,"w")
                            data = f.read().splitlines()


                            for line in data:
                                if len(line)>length:
                                    length =len(line)
                                wordb = word_tokenize(line)
                                tags = english_postagger.tag(wordb)
                                pos.write(str(line.strip()))
                                pos.write("@#%^&*")
                                for tgpair in tags:
                                    pos.write(str(tgpair[1]))
                                    pos.write("\t")
                                pos.write("\n")


                               # print i
                               # i=i+1
                               # print length


                      #  continue;