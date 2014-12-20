## feature.py
## Author: Yangfeng Ji
## Date: 08-29-2014
## Time-stamp: <yangfeng 11/06/2014 14:35:59>

from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk import WordNetLemmatizer
class FeatureGenerator(object):
    def __init__(self, stack, queue, doclen=None):
        """ Initialization of feature generator

        :type stack: list
        :param stack: list of SpanNode instance

        :type queue: list
        :param queue: list of SpanNode instance

        :type doclen: int
        :param doclen: document length wrt EDUs
        """
        # Stack
        if len(stack) >= 2:
            self.stackspan1 = stack[-1] # Top-1st on stack
            self.stackspan2 = stack[-2] # Top-2rd on stack
        elif len(stack) == 1:
            self.stackspan1 = stack[-1]
            self.stackspan2 = None
        else:
            self.stackspan1, self.stackspan2 = None, None
        # Queue
        if len(queue) > 0:
            self.queuespan1 = queue[0] # First in queue
        else:
            self.queuespan1 = None
        # Document length
        self.doclen = doclen


    def features(self):
        """ Main function to generate features

        1, if you add any argument to this function, remember
           to give it a default value
        2, if you add any sub-function for feature generation,
           remember to call the sub-function here
        """
        features = []
        # Status features
        for feat in self.status_features():
            features.append(feat)
        # Structural features
        for feat in self.structural_features():
            features.append(feat)
            # Lexical features
        for feat in self.lexical_features():
            features.append(feat)
        return features
    

    def structural_features(self):
        """ Structural features
        """
        features = []
        if self.stackspan1 is not None:
            # Span Length wrt EDUs
            features.append(('StackSpan1','Length-EDU',self.stackspan1.eduspan[1]-self.stackspan1.eduspan[0]+1))
            # Distance to the beginning of the document wrt EDUs
            features.append(('StackSpan1','Distance-To-Begin',self.stackspan1.eduspan[0]))
            # Distance to the end of the document wrt EDUs
            if self.doclen is not None:
                features.append(('StackSpan1','Distance-To-End',self.doclen-self.stackspan1.eduspan[1]))
        if self.stackspan2 is not None:
            features.append(('StackSpan2','Length-EDU',self.stackspan2.eduspan[1]-self.stackspan2.eduspan[0]+1))
            features.append(('StackSpan2','Distance-To-Begin',self.stackspan2.eduspan[0]))
            if self.doclen is not None:
                features.append(('StackSpan2','Distance-To-End',self.doclen-self.stackspan2.eduspan[1]))
        if self.queuespan1 is not None:
            features.append(('QueueSpan1','Distance-To-Begin',self.queuespan1.eduspan[0]))
        # Should include some features about the nucleus EDU
        for feat in features:
            yield feat
        

    def status_features(self):
        """ Features related to stack/queue status
        """
        features = []
        if (self.stackspan1 is None) and (self.stackspan2 is None):
            features.append(('Empty-Stack'))
        elif (self.stackspan1 is not None) and (self.stackspan2 is None):
            features.append(('One-Elem-Stack'))
        elif (self.stackspan1 is not None) and (self.stackspan2 is not None):
            features.append(('More-Elem-Stack'))
        else:
            raise ValueError("Unrecognized status in stack")
        if self.queuespan1 is None:
            features.append(('Empty-Queue'))
        else:
            features.append(('NonEmpty-Queue'))
        for feat in features:
            yield feat


    def lexical_features(self):
        """ Lexical features
        """
        features = []
        # Add the first token from the top-1st span on stack
        if self.stackspan1 is not None:
            text = self.stackspan1.text
            texts1 = word_tokenize(text)
          #  print texts1
            sent_tokenize_list =sent_tokenize(text)
            wordb = word_tokenize(sent_tokenize_list[0] )
            worde = word_tokenize(sent_tokenize_list[-1] )
       #     print wordb[0]
            features.append(('StackSpan1','BEGIN-WORD-STACK1',wordb[0].lower()))
            features.append(('StackSpan1','BEGIN-END-STACK1',worde[-1].lower()))
            features.append(('StackSpan1','BEGIN-END-WORD-STACK1',wordb[0].lower(),worde[-1].lower()))


        if self.stackspan2 is not None:
            text = self.stackspan2.text
            texts2 = word_tokenize(text)
          #  print texts1
            sent_tokenize_list =sent_tokenize(text)
            wordb = word_tokenize(sent_tokenize_list[0] )
            worde = word_tokenize(sent_tokenize_list[-1] )
       #     print wordb[0]
            features.append(('StackSpan2','BEGIN-WORD-STACK2',wordb[0].lower()))
            features.append(('StackSpan2','BEGIN-END-STACK2',worde[-1].lower()))

        if self.queuespan1 is not None:
            text = self.queuespan1.text
            textq1 = word_tokenize(text)
          #  print texts1
            sent_tokenize_list =sent_tokenize(text)
            wordb = word_tokenize(sent_tokenize_list[0] )
            worde = word_tokenize(sent_tokenize_list[-1] )
       #     print wordb[0]
            features.append(('QueueSpan1','BEGIN-WORD-QUEUE1',wordb[0].lower()))
            features.append(('QueueSpan1','BEGIN-END-QUEUE',worde[-1].lower()))
            features.append(('QueueSpan1','BEGIN-END-WORD-QUEUE1',wordb[0].lower(),worde[-1].lower()))


        if self.stackspan2 is not None and self.stackspan1 is not None:
             features.append(('StackSpan1','LENGTH-STACK1-STACK2',len(texts1),len(texts2)))
        if self.queuespan1 is not None and self.stackspan1 is not None :

            features.append(('StackSpan1','LENGTH-STACK1-QUEUE1',len(texts1),len(textq1)))
       #     features.append(('StackSpan1','POS-START-STACK1-QUEUE1',begins1,beginq1))

        for feat in features:
            yield feat
            
        
