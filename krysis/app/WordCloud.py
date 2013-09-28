import sys
from itertools import *

import requests
import simplejson as json
import MySQLdb
import os
import math

import pprint
import string
import re


class WordCloud:

	location = ""
	keywords = [] #array of strings
	
	def __init__(self,words,location):
		keywords = words
		location = location

	def generate_cloud(self,words):
		textblock = []
		for w in words:
			textblock = textblock + w
		#NEED REAL CODE FOR API
		MakeWordCloud(textblock)

		

	def main(words_from_SQL, location):
		wc = WorldCloud(words_from_SQL, location)