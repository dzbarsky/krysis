from django.http import HttpResponse
from django.shortcuts import render
from TweetProcessor import TweetProcessor
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
   text = Text(text=body, sender=sender)
   text.save() 
   tp = TweetProcessor(body)
   words = tp.part_of_speech_tags()
   for word in words:
      keyword = Keyword(word=word)
      keyword.save()
      text.keywords.add(keyword) 
   return HttpResponse()

def call(request):
   return HttpResponse()

def getTexts(request):
   texts = Text.objects.all()
   jsonified = serializers.serialize('json', texts)
   return HttpResponse(jsonified)
