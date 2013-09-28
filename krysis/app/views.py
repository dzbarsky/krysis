from django.http import HttpResponse
from django.shortcuts import render
from TextProcessor import TextProcessor
import json
from django.core import serializers
from app.models import Tweet, Text, Keyword

def index(request):
   tweets = Tweet.objects.all()
   texts = Text.objects.all()
   feed = { 'tweets' : tweets,
            'texts' : texts }
   return render(request, 'app/index.html', feed)

def sms(request):
   body = request.POST['Body']
   sender = request.POST['From']
   tp = TextProcessor(body)
   words = tp.part_of_speech_tags()
   location = ''
   for prop in words['proper']:
      location += prop + " "
   text = Text(text=body, sender=sender, location=location)
   text.save() 
   for word in words['nouns']:
      keyword = Keyword(word=word)
      keyword.save()
      text.keywords.add(keyword) 
   return HttpResponse()

def call(request):
   return HttpResponse()

def getTexts(request):
   texts = Text.objects.all()
   jsonified = serializers.serialize('json', texts)
   words = {}
   for text in texts:
       for keyword in text.keywords.all():
          lc = keyword.word.lower() 
          if lc in words:
             words[lc] += 1
          else:
             words[lc] = 1
   wordjson = json.dumps(words)
   resp = [jsonified, wordjson]
   toreturn = json.dumps(resp)
   return HttpResponse(toreturn)
