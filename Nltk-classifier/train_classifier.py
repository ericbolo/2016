#!/usr/bin/python2
from __future__ import print_function, division
from utils import normalize_text, document_type, model_filename, data_filename, \
    data_dir, event_names, keywords, get_category
from gensim.models import Doc2Vec
from collections import namedtuple
import gensim
import numpy as np
import nltk
import os
import logging
import json
import random
import cPickle
import re
from sklearn.svm import SVC


def get_data(doc2vec_model, documents):
    data = [
        (doc2vec_model.docvecs[doc.tags[0]], doc.event)
        for doc in documents
    ]

    return zip(*data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    doc2vec_model = Doc2Vec.load(model_filename)

    with open(data_filename, 'rb') as f:
        documents = cPickle.load(f)

    train_test_ratio = 0.8

    messages = [
        ' '.join(doc.words)
        for doc in documents
    ]

    categories = {}
    for message in messages:
        category = get_category(message)
        categories.setdefault(category, []).append(message)

    # for category, keywords_ in keywords.iteritems():
    #    pass

    import IPython; IPython.embed()


    buts = [doc for doc in documents if doc.event == 'BUT']
    riens = [doc for doc in documents if doc.event == 'rien'][:len(buts)]
    documents = buts + riens
    random.shuffle(documents)

    train_size = int(len(documents) * train_test_ratio)
    train_set = documents[:train_size]
    test_set = documents[train_size:]

    model = SVC(kernel='linear', gamma=1e-6)
    X, y = get_data(doc2vec_model, train_set)
    X = np.reshape(X, [-1, 100])

    #import IPython; IPython.embed()
    model.fit(X, y)

    X_test, y_test = get_data(doc2vec_model, test_set)

    predictions = model.predict(np.reshape(X_test, [-1, 100]))
    print(predictions)
    import IPython; IPython.embed()
