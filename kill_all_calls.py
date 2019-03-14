# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import twilio_credentials



def main():

    client = Client(twilio_credentials.account_sid, twilio_credentials.auth_token)

    for call in client.calls.list(status='in-progress'):
        call.update(status='completed')


if __name__ == '__main__':
    main()
