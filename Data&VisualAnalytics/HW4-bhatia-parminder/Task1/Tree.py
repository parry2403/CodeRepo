# CSE6242/CX4242 Homework 4 Pseudocode
# You can use this skeleton code for Task 1 of Homework 4.
# You don't have to use this code. You can implement your own code from scratch if you want.

import csv
from collections import Counter;
from collections import defaultdict;
import math;
from pprint import pprint
# Implement your decision tree below

numeric =[]
continuous= defaultdict(float)
mean = Counter()
err =0

class DecisionTree():
        tree = {}

        def learn(self, training_set):
            self.tree = buildTree(training_set,range(len(training_set[0])-1),opti = None)
        #    pprint( self.tree)
        def classify(self, test_instance):

            output =  classification(self.tree,test_instance)

            return output


def classification(tree, data):
    if not tree :
        return None
    if not isinstance(tree, dict):
        return tree
    key = tree.keys()[0]
    values = tree.values()[0]
    dataValue = data[key]

    if not dataValue.isdigit() and dataValue not in values:
      #  print dataValue
     #   print key
      #  print 'here*******'
    #    print values.keys()
        majority = Counter()
        for key in values.keys():
            if values[key]== '<=50K':
                majority['<=50K']+=1
            if values[key]== '>50K':
                majority['>50K']+=1
    #    errr =errr+1
      #  print err
      #  err = err + 1
     #   print tree.get(key)
       # mostCommon(values.values())
        if len(majority)==0:
            mkey  = values.values()[0]
            return  classification(mkey,data);
        return majority.most_common()[0][0]


    if not dataValue.isdigit():
        return classification(values[dataValue],data)
    if dataValue.isdigit():
            if len(values) ==1:
                 return classification(values.values()[0],data)
            if float(dataValue)<=mean[key]:
                return classification(values['LE'],data)
            else:
                return classification(values['G'],data)






def buildTree(data,attributes,opti):
    #     print attributes
         if not data or not attributes:
             return opti

         class_count,mostCommonIndex = mostCommon(data)
         opti = mostCommonIndex
         if len(data) < 16:
             return opti
         if len(class_count) == 1:
             return mostCommonIndex
         bestNode = bestAttribute(data,attributes)
         if bestNode == -1 :
            return opti

         remainingAttributes =  [i for i in attributes if i != bestNode]
         nodeTree = {bestNode:{}}
         partitions= distribute(data,bestNode)
         for keys in partitions.keys():
             nodeTree[bestNode][keys] = buildTree(partitions[keys],remainingAttributes,opti)
         return nodeTree


def entropy(data):
    H = 0.0
    total =0.0
    count  = Counter(pts[-1] for pts in data)
    for counters in count.keys():
        total = total+count[counters]

    for counters in count.keys():
        H= H-(count[counters]/total)*math.log(count[counters]/total)

    return H

def mostCommon(data):
    count  = Counter(pts[-1] for pts in data)
    mostCommon = count.most_common(1),
    mostCommonIndex = count.most_common(1)[0][0]
    return count , mostCommonIndex

def knowledgeGain(data,attribute,val=False):
    H = entropy(data)
  #  print H
    partitions = distribute(data, attribute)
    total =len(data) * 1.0
    for keys in partitions.keys():
        H = H-(len(partitions[keys])/total)*entropy(partitions[keys])

    return H

def IntrinsicGain(data,attribute,val=False):
    H = entropy(data)
  #  print H
    partitions = distribute(data, attribute)
    total =len(data) * 1.0
    for keys in partitions.keys():
   #     print keys
        H = H-(len(partitions[keys])/total)*math.log(len(partitions[keys])/total)
   # print H
    return H
def GainRatio(data,attribute):
    return knowledgeGain(data,attribute)/IntrinsicGain(data,attribute)

def bestAttribute(data,attributes):
    I =0.0
    best =-1
    for attribute in attributes:
 #       print attribute
       # gain = knowledgeGain(data,attribute)
        gain = GainRatio(data,attribute)
      #  print gain
        if gain > I:
            best=attribute
            I = gain

    return best

def distribute(data, attribute):
    partitions = defaultdict(list)
    if numeric[attribute]:
        for pts in data:
            if float(pts[attribute])<=mean[attribute]:
                 partitions['LE'].append(pts)
            else:
                 partitions['G'].append(pts)

    else:
        for pts in data:
            partitions[pts[attribute]].append(pts)
    return partitions

def run_decision_tree():
	
        # Load data set
        with open("hw4-task1-data.tsv") as tsv:
            data = [tuple(line) for line in csv.reader(tsv, delimiter="\t")]
        print "Number of records: %d" % len(data)


        # Split training/test sets
        # You need to modify the following code for cross validation.
        K = 10
        av_acc=0.0
        f = open("result.txt", "w")
        for cross in range(K):

            training_set = [x for i, x in enumerate(data) if i % K != cross]
            test_set = [x for i, x in enumerate(data) if i % K == cross]

            for attribute in data[0]:
                if attribute.isdigit():
                    numeric.append(True)
                else:
                    numeric.append(False)
     #       print numeric

            for pts in data:
                for attribute in range(len(pts)):
                    if numeric[attribute]:
                          mean[attribute]+=int(pts[attribute])

            for key in mean.keys():
                mean[key] = mean[key]/len(data)

            tree = DecisionTree()
            # Construct a tree using training set
            tree.learn( training_set )
        #    partitions = distribute(data,1)

            # Classify the test set using the tree we just constructed
            results = []
            for instance in test_set:
                result = tree.classify( instance[:-1] )
                results.append( result == instance[-1] )

            # Accuracy
            accuracy = float(results.count(True))/float(len(results))
            av_acc =av_acc+accuracy
            output ="accuracy", cross, ":  %.4f"   % accuracy
            print output
            f.write(str(output))

            # Writing results to a file (DO NOT CHANGE)


        av_acc = av_acc/10
        foutput ="Average Accuracy: %.4f" % av_acc
        print foutput


            # Writing results to a file (DO NOT CHANGE)

        f.write(str(foutput))
        f.close()
if __name__ == "__main__":
	run_decision_tree()
