import sys
from itertools import *

import requests
import simplejson as json
import MySQLdb
import os
import math

import pprint
import nltk
import string
import re

class TextProcessor:

  sourceText = ""

  def __init__(self,text):
    self.sourceText = text

  def part_of_speech_tags(self):
    # Strip punctuation
    text = ''.join(ch for ch in self.sourceText if ch not in string.punctuation)
    text = nltk.word_tokenize(text)
    output_tuples = nltk.pos_tag(text);
    return self.find_nouns(output_tuples)

  #find nouns in part-of-speech tagged text add to keywords table
  def find_nouns(self, output_tuples):
    text_words = {'proper': [], 'nouns': []}
    for item in output_tuples:
      if item[1] in ("NP", "NNP"):
         text_words['proper'].append(item[0])
      if item[1] in ("NN", "NNP", "NNS"):
         text_words['nouns'].append(item[0])
    return text_words
