#!/usr/bin/env python3
from flask import Flask, jsonify, request
from character import Character
from souputils import SoupUtils
import constants
import os
import requests

app = Flask(__name__)
character = Character()
soup_utils = SoupUtils()
API_URL = constants.STARDEW_WIKI
SEARCH_API = constants.SEARCH_API

@app.route('/api/v1/birthday', methods=['GET'])
def get_birthday():
    name = request.args.get('name')
    return jsonify(_get_birthday(name))

def _get_birthday(name):
    url = f'{API_URL}{SEARCH_API}{name}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    search_success = soup_utils.was_search_successful(soup)
    if search_success:
        # TODO HANDLE when a character isn't passed in. i.e. barn. Right now it just asks you to repeat yourself.

        birthday = character.get_birthday(soup)
        return {'birthday': birthday}
    else:
        return {'birthday': f'Name {name} not found'}

@app.route('/api/v1/best_gifts', methods=['GET'])
def get_best_gifts():
    name = request.args.get('name')
    return jsonify(_get_best_gifts(name))

def _get_best_gifts(name):
    url = f'{API_URL}{SEARCH_API}{name}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    search_success = soup_utils.was_search_successful(soup)
    if search_success:
        # TODO HANDLE when a character isn't passed in. i.e. barn. Right now it just asks you to repeat yourself.

        best_gifts = character.get_best_gifts(soup)
        return {'best_gifts': best_gifts}
    else:
        return {'best_gifts': f'Name {name} not found'}

@app.route('/api/v1/post_fulfillment', methods=['POST'])
def post_fulfillment():
    data = request.get_json()
    intent = data.get('queryResult').get('action')
    name_param = data.get('queryResult').get('parameters').get('name')

    if intent == 'birthday':
        response = _get_birthday(name_param).get('birthday')
    elif intent == 'best_gifts':
        response = _get_best_gifts(name_param).get('best_gifts')

    response_dict = {
        'fulfillmentText' : response
    }
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
