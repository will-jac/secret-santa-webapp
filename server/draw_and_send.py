import json

from do_drawing import pair
from send_mail import send_mail

with open('participants.json', 'r') as f:
    participants = json.load(f)

pairing = pair(len(participants))

message_template = '''Ho Ho Ho!
Welcome to the Williams' family Secret Santa Drawing!

{santa_name}, you have drawn: {gift_name}

Don't tell anyone! Good luck!
'''

for i, p in enumerate(pairing):
    santa = participants[i]
    gift = participants[p]
    
    send_mail(
        santa[1],
        santa[0],
        'Williams Family Secret Santa',
        message_template.format(santa_name=santa[0], gift_name=gift[0])
    )
