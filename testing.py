# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import twitter
import MySQLdb
import os
import time
import datetime

def executeQuery(sql):
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print "\n~~~~~~~~QUERY FAILED: " + sql
        print e
        db.rollback()
        return None

def escape(val):
    return val.replace("'", "\\'")

account_sid = "AC0e0571d94d5d6dba4ac914247086bde1"
auth_token = "1048a4e4a412d86677011b93d0300995"
client = TwilioRestClient(account_sid, auth_token)

db = MySQLdb.connect("localhost", "root", "", "krysis" )
executeQuery("drop database krysis;")
executeQuery("create database krysis;")
os.system("python krysis/manage.py syncdb")
executeQuery("use krysis")

for sms in client.sms.messages.list():
    sql = """INSERT INTO app_text(text, sender, date)
             VALUES('%s', '%s', '%s')
          """ % (escape(sms.body), sms.to, sms.date_sent)
    executeQuery(sql)

consumer_key='fVHE2OyTytlxzWiSAvk3w'
consumer_secret='GwJ6A72AHTIzPpPmHBdVKeEqWrlCxT47xUxLoXaBMWA'
access_token_key='1912820988-iKkJ27a0XMUISHUo2GGuMAXEurOzBBisHwFV7l5'
access_token_secret='fFKveSq1JpFdnxSNkmEc53IQ7Bk88VXXnT8g5iVfM'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

for tweet in api.GetMentions():
    sql = """INSERT INTO app_tweet(text, sender, date)
             VALUES('%s', '%s', '%s')
          """ % (escape(tweet.text),
                 escape(tweet.user.name),
                 tweet.created_at)
    executeQuery(sql)

