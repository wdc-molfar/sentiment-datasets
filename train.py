#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import fasttext

hyper_params = { 
    "lr": 0.35,         # Learning rate
    "epoch": 100,       # Number of training epochs to train for
    "wordNgrams": 3,    # Number of word n-grams to consider during training
    "dim": 155,         # Size of word vectors
    "ws": 5,            # Size of the context window for CBOW or skip-gram
    "minn": 3,          # Min length of char ngram
    "maxn": 20,          # Max length of char ngram
    "bucket": 2014846,  # Number of buckets
}

def trainer(trainFile: str, model_path: str, hyper_params: dict) -> None:
    model = fasttext.train_supervised(input=trainFile,   label_prefix='__label__') # **hyper_params,
    print("FastText model trained with hyperparameters: \n {0}".format(hyper_params))
    # Quantize model to reduce space usage
    model.quantize(input=None,
                      qout=False,
                      cutoff=0,
                      retrain=False,
                      epoch=None,
                      lr=None,
                      thread=None,
                      verbose=None,
                      dsub=2,
                      qnorm=False,
                     )
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    # Save a quantized model
    model.save_model(os.path.join(model_path, lang+".ftz"))

if __name__ == "__main__":
    lang = sys.argv[1] #format of input languale is "uk", "ru" or "en"
    trainer(os.getcwd()+'/train/'+lang+'.txt', 'models', hyper_params)       
