# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import twitter

account_sid = "AC0e0571d94d5d6dba4ac914247086bde1"
auth_token = "1048a4e4a412d86677011b93d0300995"
client = TwilioRestClient(account_sid, auth_token)

sms_list = client.sms.messages.list()
print sms_list
print sms_list[0]
print sms_list[0].body
print sms_list[1]
print sms_list[1].body
print "hu"

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

print api.GetMentions()[0].text

# When we want headphones...uncomment these lines!
# for i in range(100):
#   api.PostUpdate('Let me know if you have a crisis! %i people have already reported!  #hackthechange @hackthechange13' % i)
