from twilio.rest import Client
import schedule, time, random

cellphone = yourNumber
twilio_number = twilio_assigned_by_twilio

'''1. messages'''

nightTime_quotes = [
    "Time to get ready for bed",
    "Let's watch a movie, ok?",
    "Are you still in the washroom?",
    "Love you"
]

night_quote = nightTime_quotes[random.randint(0,len(nightTime_quotes) - 1)]

morningTime_quotes = [
    "Good morning babe",
    "Rise and shine",
    "Babe, time to get up",
    "If you're making a coffee, can you make one for me, too?"
]

morning_quote = morningTime_quotes[random.randint(0, len(morningTime_quotes) - 1)]

'''2. send messages function'''

def send_message(quote):
    account = "enter_twilio_account_here"
    token = "enter_twilio_token_here"
    client = Client(account, token)

    client.messages.create(
        to=cellphone,
        from_=twilio_number,
        body=quote
    )

'''3. scheduler'''
schedule.every().day.at("2230").do(send_message, night_quote)
schedule.every().day.at("0930").do(send_message, morning_quote)

while True:

    # Checks whether a schedule task
    # is pending to run

    schedule.run_pending()
    time.sleep(1)
