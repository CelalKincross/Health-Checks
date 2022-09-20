'''1. messages'''

messages_array = [
    "Time to get ready for bed",
    "Let's watch a movie, ok?"
]

'''2. send messages function'''
from twilio.rest import Client
import schedule 
import random

cellphone = enterphone_here
twilio_number = entertwiliophonehere8


def send_message(quote):
    account = "acc#"
    token = "token#"
    client = Client(account, token)

    client.messages.create(
        to=cellphone,
        from_=twilio_number,
        body=quote
    )

'''3. scheduler'''
quote = messages_array[random.randint(0,len(messages_array))]
schedule.every().day.at("22:30").do(send_message, quote)


