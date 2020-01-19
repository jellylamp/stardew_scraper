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

    url = f'{API_URL}{SEARCH_API}{name}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    search_success = soup_utils.was_search_successful(soup)
    if search_success:
        # TODO HANDLE when a character isn't passed in. i.e. barn

        birthday = character.get_birthday(soup)
        return jsonify({'birthday': birthday})
    else:
        return jsonify({'error': f'Name {name} not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
