# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import twilio_credentials
import argparse

# Your Account Sid and Auth Token from twilio.com/console
#account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


playbooks={
    # this will send DTMF '1'
    'playbook_2': 'https://handler.twilio.com/twiml/EH21752ca7833091a46f2afc74eb05cac3',
}

def make_call(callee_number, playbook_url=playbooks['playbook_2']):
    client = Client(twilio_credentials.account_sid, twilio_credentials.auth_token)

    call = client.calls.create(
        #url='https://gist.githubusercontent.com/sli-cs/452c15d2dfa4dfe871af0f9604a6edc8/raw/3e842f717510e7560a13ec4055a8d09e2a8bcc14/test_twml.xml',
        url=playbook_url,
        to=callee_number,
        from_=twilio_credentials.from_number
        )

    return

    pass

def main():

    parser = argparse.ArgumentParser(description='call someone!')
    parser.add_argument('callee_number', help='the number to call')

    args = parser.parse_args()  # returns data from the options specified (echo)
    make_call(args.callee_number)


if __name__ == '__main__':
    main()