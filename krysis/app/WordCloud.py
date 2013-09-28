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
   keywords = [] # array of strings
   
   def __init__(self,words):
      keywords = words

   def generate_cloud(self,words):
      textblock = []
      for w in words:
         textblock = textblock + w
      MakeWordCloud(textblock)
