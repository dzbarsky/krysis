from django.http import HttpResponse
from django.shortcuts import render
from TextProcessor import TextProcessor
import json
from django.core import serializers
from app.models import Tweet, Text, Keyword
import twitter
from twilio.rest import TwilioRestClient

def escape(val):
    return val.replace("'", "\\'")

def getNewTweets():
  consumer_key='fVHE2OyTytlxzWiSAvk3w'
  consumer_secret='GwJ6A72AHTIzPpPmHBdVKeEqWrlCxT47xUxLoXaBMWA'
  access_token_key='1912820988-iKkJ27a0XMUISHUo2GGuMAXEurOzBBisHwFV7l5'
  access_token_secret='fFKveSq1JpFdnxSNkmEc53IQ7Bk88VXXnT8g5iVfM'

  api = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token_key,
                    access_token_secret=access_token_secret)

  existingtweets = [t.text for t in Tweet.objects.all()]
  for tweet in api.GetMentions():
    if not tweet.text in existingtweets:
      tp = TextProcessor(tweet.text)
      words = tp.part_of_speech_tags()
      location = ''
      for prop in words['proper']:
        location += prop + " "
      obj = Tweet(text=tweet.text, sender=tweet.user.name, location=location)
      obj.save()
      for word in words['nouns']:
        keyword = Keyword(word=word)
        keyword.save()
        obj.keywords.add(keyword)

def index(request):
   getNewTweets()
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

   account_sid = "AC0e0571d94d5d6dba4ac914247086bde1"
   auth_token = "1048a4e4a412d86677011b93d0300995"
   client = TwilioRestClient(account_sid, auth_token)
   message = client.messages.create(body="Thanks for your crisis report! Stay safe.",
       to=sender, from_="+19292274747")
   print message.sid

   return HttpResponse()

def call(request):
   return HttpResponse()

def getKeywords(objects):
   words = {}
   for obj in objects:
       for keyword in obj.keywords.all():
          lc = keyword.word.lower() 
          if lc in words:
             words[lc] += 1
          else:
             words[lc] = 1
   return words

def getTexts(request):
   texts = Text.objects.all()
   jsonified = serializers.serialize('json', texts)
   textwords = getKeywords(texts)
   tweetwords = getKeywords(Tweet.objects.all())
   words = dict(textwords, **tweetwords)
   wordjson = json.dumps(words)
   resp = [jsonified, wordjson]
   toreturn = json.dumps(resp)
   return HttpResponse(toreturn)
