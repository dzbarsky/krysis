from django.http import HttpResponse
from django.shortcuts import render

from app.models import Tweet, Text

def index(request):
   tweets = Tweet.objects.all()
   texts = Text.objects.all()
   feed = { 'tweets' : tweets,
            'texts' : texts }
   return render(request, 'app/index.html', feed)

def sms(request):
   print request.POST
   return HttpResponse()

def call(request):
   if not request.is_ajax():
      print 'not ajax?'
      return HttpResponse()
   data = request.POST
   print data
   return HttpResponse()
