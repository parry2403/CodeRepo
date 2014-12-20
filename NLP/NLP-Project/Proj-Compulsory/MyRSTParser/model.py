## model.py
## Author: Yangfeng Ji
## Date: 09-09-2014
## Time-stamp: <yangfeng 11/05/2014 20:44:25>
## Last changed: umashanthi 11/19/2014 

""" As a parsing model, it includes the following functions
1, Mini-batch training on the data generated by the Data class
2, Shift-Reduce RST parsing for a given text sequence
3, Save/load parsing model
"""

from sklearn.svm import LinearSVC
from cPickle import load, dump
from parser import SRParser
from feature import FeatureGenerator
from tree import RSTTree
from util import *
from datastructure import ActionError
import gzip, sys
import numpy as np
from collections import defaultdict
class ParsingModel(object):
    def __init__(self, vocab=None, idxlabelmap=None, clf=None):
        """ Initialization
        
        :type vocab: dict
        :param vocab: mappint from feature templates to feature indices

        :type idxrelamap: dict
        :param idxrelamap: mapping from parsing action indices to
                           parsing actions

        :type clf: LinearSVC
        :param clf: an multiclass classifier from sklearn
        """
        self.vocab = vocab
        # print labelmap
        self.labelmap = idxlabelmap
        if clf is None:
            self.clf = LinearSVC()


    def train(self, trnM, trnL):
        """ Perform batch-learning on parsing model
        """
        self.clf.fit(trnM, trnL)


    def predict(self, features):
        """ Predict parsing actions for a given set
            of features

        :type features: list
        :param features: feature list generated by
                         FeatureGenerator
        """
        vec = vectorize(features, self.vocab)
        predicted_output = self.clf.decision_function(vec)
        idxs = np.argsort(predicted_output[0])[::-1]
        possible_labels = []
        for index in idxs:
            possible_labels.append(self.labelmap[index])
        return possible_labels



    def savemodel(self, fname):
        """ Save model and vocab
        """
        if not fname.endswith('.gz'):
            fname += '.gz'
        D = {'clf':self.clf, 'vocab':self.vocab,
             'idxlabelmap':self.labelmap}
        with gzip.open(fname, 'w') as fout:
            dump(D, fout)
        print 'Save model into file: {}'.format(fname)


    def loadmodel(self, fname):
        """ Load model
        """
        with gzip.open(fname, 'r') as fin:
            D = load(fin)
        self.clf = D['clf']
        self.vocab = D['vocab']
        self.labelmap = D['idxlabelmap']
        print 'Load model from file: {}'.format(fname)


    def sr_parse(self, texts,fname):
        """ Shift-reduce RST parsing based on model prediction

        :type texts: list of string
        :param texts: list of EDUs for parsing
        """
        # Initialize parser
        srparser = SRParser([],[])

        dep = defaultdict()
        pos = defaultdict()
        lines =defaultdict()
   # print fname.split(".dis")[0]+'.dep'
        dir = fname.split

        s =fname.split(".edus")
 #   print fname
  #  st= fname
        if fname.endswith(".out.edus"):
         #   print "yes"
            s= fname.split(".out.edus")


        f= open(s[0]+'.dep',"r")
        data = f.read().splitlines()
        for line in data:
        #   print line
           l = line.split('@#%^&*')
           dep[l[0]] = l[1]

        f= open(s[0]+'.pos',"r")
        data = f.read().splitlines()
        for line in data:
        #   print line
               l = line.split('@#%^&*')
               pos[l[0]] = l[1].strip()
        f= open(s[0]+'.line',"r")
        data = f.read().splitlines()
        for line in data:
        #   print line
               l = line.split('@#%^&*')
               lines[l[0]] = l[1]





        srparser.init(texts,pos,dep,lines)
        # Parsing
        while not srparser.endparsing():
            # Generate features
            stack, queue = srparser.getstatus()
            # Make sure call the generator with
            # same arguments as in data generation part
            fg = FeatureGenerator(stack, queue)
            features = fg.features()
            labels = self.predict(features)
            # Enumerate through all possible actions ranked based on predcition scores
            for i,label in enumerate(labels):
                action = label2action(label)                
                try:
                    srparser.operate(action)
                    break # if legal action, end the loop
                except ActionError:
                    if i < len(labels): # if not a legal action, try the next possible action
                        continue
                    else:               
                        print "Parsing action error with {}".format(action)
                        sys.exit()
  
        tree = srparser.getparsetree()
        rst = RSTTree(tree=tree)
        return rst
            
