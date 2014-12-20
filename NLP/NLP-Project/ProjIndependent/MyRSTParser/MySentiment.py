__author__ = 'Parry'
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import csv
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
import numpy
from sklearn.feature_extraction.text import CountVectorizer
import random
from sklearn import metrics
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
def features():
    features= []
    for feat in features:
            yield feat


if __name__ == '__main__':
    # Create data for offline training
    clf = LinearSVC()
    print 'Create data ...'
    createdata(path="./train_data")
    # Train a parsing model
    print 'Training a parsing model ...'
    trainmodel()
    # Evaluate on dev/test documents
    print 'Evaluating the parsing performance ...'
    evalparser(path='./dev_data', report=True)