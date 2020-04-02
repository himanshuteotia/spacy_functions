#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:53:31 2020

@author: himanshu teotia
@description Spacy functions

"""


def import_eng_class():
    # Import the English language class
    from spacy.lang.en import English
    # Create the nlp object
    nlp = English()
    return nlp

def print_doc_object(text,nlp):
    doc = nlp(text)
    for token in doc:
        print(token.text)