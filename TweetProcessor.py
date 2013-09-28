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


	def __init__(self,tweet,latLong):
   		sourceTweet = tweet
   		latitude = latLong[0]
   		longitutde = latLong[1]


   	def part_of_speech_tags(self):
    # Strip punctuation
    text = ''.join(ch for ch in sourceTweet if ch not in string.punctuation)
    text = nltk.word_tokenize(text)
    output_tuples = nltk.pos_tag(text);
    self.find_nouns(output_tuples)


    #find nouns in part-of-speech tagged tweet add to keywords table
   	def find_nouns(self, output_tuples):
        for item in output_tuples:
            if item[1] in ("NN", "NNP", "NNS"):
            	pass
            	#STORE THIS WORD IN KEYWORDS TABLE AND KEYWORD-TWEET PIVOT TABLE
                #sql="""INSERT IGNORE INTO krysis_keyword(word) VALUES ('%s')""" % item[0]
                #self.executeQuery(sql)



def main(tweets,latLong):
    tp = TweetProcessor(tweet,latLong)
    tp.part_of_speech_tags()


