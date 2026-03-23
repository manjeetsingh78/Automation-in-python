from twilio.rest import Client
import os
from dotenv import load_dotenv
import time

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')


client = Client(account_sid, auth_token)
while True:
    message = client.messages.create(
      from_='+15074286866',
      body='Hi this message is from Manjeet singh',
      to='+917830462797'
    )
    print(message.sid)
    time.sleep(60)