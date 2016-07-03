#!/usr/bin/python3
#from http.server import HTTPServer, BaseHTTPRequestHandler
#from urllib.parse import parse_qs, urlparse

VALIDATION_TOKEN = 'random1246'
PAGE_ACCESS_TOKEN = 'EAAB6Sm8cmPoBAOcgLZA1ri0ACysxuxE6H3PR7oZBxKuFK4F5nepCzmPmSP5pNKgneDyRk59X6oZC00AasZBhdhpwmhm0GTxsl7jlWqjLc5uAVeDhSpcOkKZAlE0flZADNYLEhDGcVBQP8ZBiFGJmUO7r0gyZAYVhp888r0em0YrDSQZDZD'

from flask import Flask, request
import requests
import logging
import json

app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def handle_request():
    logging.debug('request: %s', request)
    logging.debug('request data: %s', request.data)
    logging.debug('request args: %s', request.args)
    logging.debug('request json: %s', request.json)

    if request.method == 'GET':
        data = request.args
        if (data.get('hub.mode') == 'subscribe' and
                data.get('hub.verify_token') == VALIDATION_TOKEN):
            logging.info('validating webhook')
            return data.get('hub.challenge')
        else:
            logging.warning('error')
    elif request.method == 'POST':
        data = request.json
        for entry in data.get('entry', []):
            for event in entry.get('messaging', []):
                handle_event(event)


def handle_event(event):
    sender_id = event['sender']['id']
    message_text = event['message']['text']

    logging.debug('received message from %s, content: %s', sender_id,
                  message_text)

    reply = get_reply(sender_id, message_text)

    message_data = {
        'recipient': {'id': sender_id},
        'message': {'text': reply}
    }
    send_message(message_data)


def send_message(message_data):
    url = 'https://graph.facebook.com/v2.6/me/messages'
    message_data['access_token'] = PAGE_ACCESS_TOKEN
    res = requests.post(url, data=message_data)
    logging.debug('server reply: %s', res)


def get_reply(sender_id, text):
    return 'Hi!'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run()
