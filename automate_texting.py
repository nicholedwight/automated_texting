from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number
import schedule, random, time

GOOD_MORNING_QUOTES = [
    "Good morning!",
    "Rise and shine, sleepyhead!",
    "Time to take on the day!"
]

def send_message(quote):
    account = twilio_account
    token = twilio_token
    client = Client(account,token)
    quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES)-1)]

    client.messages.create(to=cellphone,
                            from_=twilio_number,
                            body=quote)


schedule.every().day.at("13:19").do(send_message, GOOD_MORNING_QUOTES)

while True:
    schedule.run_pending()
    time.sleep(2)