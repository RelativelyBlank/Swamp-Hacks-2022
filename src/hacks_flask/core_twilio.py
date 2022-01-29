twilio_number = '17853775816'
account_sid = 'AC2a7e4994f0e017472a12f0e38874e4d2'
auth_token = 'c678201b5972960568160db332ccfbc2'

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_message(message, phone_number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=phone_number
    )
    return message.sid
