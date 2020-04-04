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

def get_doc(text,nlp):
    doc = nlp(text)
    return doc
        
def print_doc_object(text,nlp):
    doc = nlp(text)
    for token in doc:
        print(token.text)
            
def return_span(start,end,doc):
    # A slice from the Doc is a Span object
    span = doc[start:end]
    return span.text

def token_attributes(text,nlp):
    doc = nlp(text)
    print('Index:   ', [token.i for token in doc])
    print('Text:    ', [token.text for token in doc])
    print('is_alpha:', [token.is_alpha for token in doc])
    print('is_punct:', [token.is_punct for token in doc])
    print('like_num:', [token.like_num for token in doc])

token_attributes("It costs $5.", import_eng_class())


## Statistical models ##

"""
What are statistical models?
* Enable spaCy to predict linguistic attributes in context
    Part-of-speech tags
    Syntactic dependencies
    Named entities
 Trained on labeled example texts
 Can be updated with more examples to fine-tune predictions

"""
    
    