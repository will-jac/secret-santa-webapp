# a simple flask server

import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from send_mail import send_mail

app = Flask(__name__)

# TODO: better authentication
CORS(app)

@app.route('/', methods=['GET'])
def get_participants():
    print(request)
    name = request.args.get('name', default=None, type=str)
    email = request.args.get('email', default=None, type=str)

    # add the name and email to the partcipants
    participants = load_participants()

    participant_added = False

    if name is not None and email is not None and \
            name not in [p[0] for p in participants] and \
            email not in [p[1] for p in participants]:
        participants.append([name, email])
        participant_added = True

        # save the file
        write_participants(participants)

    # just check what's being returned
    print(participants)

    response = jsonify([participants, participant_added])
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def load_participants(filename='./participants.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def write_participants(participants, filename='./participants.json'):
    with open(filename, 'w') as f:
        return json.dump(participants, f)

if __name__ == '__main__':
    # load the data initially
    app.run()
    
