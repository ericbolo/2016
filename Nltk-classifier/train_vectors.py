#!/usr/bin/python2
from __future__ import print_function, division
from utils import normalize_text, document_type, model_filename, data_filename, \
    data_dir, event_names
from gensim.models import Doc2Vec
from collections import namedtuple
import gensim
import nltk
import os
import logging
import json
import random
import cPickle


def load_data(filenames, event_names):
    data = {}

    for filename, event_name in zip(filenames, event_names):
        with open(filename) as f:
            for i, line in enumerate(f):
                try:
                    js = json.loads(line)
                    if 'text' in js:
                        data_ = data.setdefault(event_name, [])
                        data_.append(js['text'])
                except ValueError:
                    pass

    return data


def train_model(data, filename, epochs=1):
    model = Doc2Vec(hs=0, negative=5, size=100, min_count=2)
    model.build_vocab(data)

    for epoch in range(epochs):
        logging.info('epoch %i', epoch)
        model.train(data)

    # v = model.infer_vector('hello world !')
    model.save(filename)
    return model


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    filenames = ['{}.json'.format(os.path.join(data_dir, name))
                 for name in event_names]
    # data = [data_[:10] for data_ in load_data(filenames).values()]
    data = load_data(filenames, event_names)

    # import IPython; IPython.embed()

    documents = []

    doc_id = 0
    for event_name, data_ in data.iteritems():
        for text in data_:
            text = normalize_text(text)
            # if 'euro2016' not in text:
            #     continue
            doc = document_type(text.split(), [doc_id], event=event_name)
            documents.append(doc)
            doc_id += 1

    logging.info('number of documents: %i', len(documents))
    random.shuffle(documents)
    # documents = documents[:1000]  # for testing

    model = train_model(documents, model_filename)
    with open(data_filename, 'wb') as f:
        cPickle.dump(documents, f)

    # import IPython; IPython.embed()