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

class TweetProcessor:

  sourceTweet = ""
  latitude = 0.0
  longitude = 0.0

  def __init__(self,tweet,latLong = [0,0]):
    self.sourceTweet = tweet
    self.latitude = latLong[0]
    self.longitude = latLong[1]

  def part_of_speech_tags(self):
    # Strip punctuation
    text = ''.join(ch for ch in self.sourceTweet if ch not in string.punctuation)
    text = nltk.word_tokenize(text)
    output_tuples = nltk.pos_tag(text);
    return self.find_nouns(output_tuples)

  #find nouns in part-of-speech tagged tweet add to keywords table
  def find_nouns(self, output_tuples):
    tweet_words = []
    for item in output_tuples:
      if item[1] in ("NN", "NNP", "NNS"):
         tweet_words.append(item[0])
         #word = Keyword(word=item[1])
         #word.save()
         #tweet = Tweet.objects.get(text=sourceTweet)
         #tweet.keywords.add(word)
    return tweet_words
      #STORE THIS WORD IN KEYWORDS TABLE AND KEYWORD-TWEET PIVOT TABLE
      #sql="""INSERT IGNORE INTO krysis_keyword(word) VALUES ('%s')""" % item[0]
      #self.executeQuery(sql)
