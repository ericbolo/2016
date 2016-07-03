#!/usr/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function, division
from utils import normalize_text, document_type, model_filename, data_filename, \
    data_dir, event_names
from gensim.models import Doc2Vec
from collections import namedtuple
import gensim
import numpy as np
import nltk
import os
import sys
import logging
import json
import random
import cPickle
from sklearn.svm import SVC
from sklearn.cluster import KMeans


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

    features = [
        doc2vec_model.docvecs[doc.tags[0]]
        for doc in documents
    ]
    features = np.reshape(features, [-1, 100]).astype(np.double)
    messages = [
        ' '.join(doc.words)
        for doc in documents
    ]

    model = KMeans(n_clusters=len(event_names))
    # model = k_means(features, len(event_names))

    predictions = model.fit_predict(features)
    # import IPython; IPython.embed()


    clusters = {}
    for prediction, message in zip(predictions, messages):
        clusters.setdefault(prediction, []).append(message)

    for cluster_id, messages in clusters.iteritems():
        # print(cluster_id)
        print('\n'.join(
            u'{}: {}'.format(cluster_id, message) for message in messages
        ).encode('utf-8'))
        print()

    # train_test_ratio = 0.8
    #
    # buts = [doc for doc in documents if doc.event == 'BUT']
    # riens = [doc for doc in documents if doc.event == 'rien'][:len(buts)]
    # documents = buts + riens
    # random.shuffle(documents)
    #
    # train_size = int(len(documents) * train_test_ratio)
    # train_set = documents[:train_size]
    # test_set = documents[train_size:]
    #
    # model = SVC(kernel='linear', gamma=1e-6)
    # X, y = get_data(doc2vec_model, train_set)
    # X = np.reshape(X, [-1, 100])
    #
    # #import IPython; IPython.embed()
    # model.fit(X, y)
    #
    # X_test, y_test = get_data(doc2vec_model, test_set)
    #
    # predictions = model.predict(np.reshape(X_test, [-1, 100]))
    # print(predictions)
    # import IPython; IPython.embed()
