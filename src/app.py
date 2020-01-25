#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_restx import Resource, Api
from character import Character
from souputils import SoupUtils
from bundles import Bundles
import constants
import os
import requests

app = Flask(__name__)
api = Api(app, version='1.0.0', title='Stardew Scraper API',
    description='An API that scrapes the Stardew Valley wiki for use with Google Home.',
)

character = Character()
soup_utils = SoupUtils()
bundles = Bundles()

@api.route('/api/v1/birthday')
class Birthday(Resource):
    """
    Given a Village name, return their birthday.
    """
    def get(self):
        name = request.args.get('name')
        return jsonify(_get_birthday(name))

def _get_birthday(name):
    url = f'{constants.STARDEW_WIKI}{constants.SEARCH_API}{name}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    search_success = soup_utils.was_search_successful(soup)
    if search_success:
        # TODO HANDLE when a character isn't passed in. i.e. barn. Right now it just asks you to repeat yourself.

        birthday = character.get_birthday(soup)
        return {'birthday': birthday}
    else:
        return {'birthday': f'Name {name} not found'}

@api.route('/api/v1/best_gifts')
class BestGifts(Resource):
    """
    Given a villager, get the their loved gifts.
    """
    def get(self):
        name = request.args.get('name')
        return jsonify(_get_best_gifts(name))

def _get_best_gifts(name):
    url = f'{constants.STARDEW_WIKI}{constants.SEARCH_API}{name}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    search_success = soup_utils.was_search_successful(soup)
    if search_success:
        # TODO HANDLE when a character isn't passed in. i.e. barn. Right now it just asks you to repeat yourself.

        best_gifts = character.get_best_gifts(soup)
        return {'best_gifts': best_gifts}
    else:
        return {'best_gifts': f'Name {name} not found'}

@api.route('/api/v1/universal_loves')
class UniversalLoves(Resource):
    """
    Returns all Universal Loves.
    """
    def get(self):
        return jsonify(_get_universal_loves())

def _get_universal_loves():
    url = f'{constants.STARDEW_WIKI}{constants.UNIVERSAL_LOVES}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    universal_loves = character.get_universal_loves(soup)
    return {'universal_loves': universal_loves}

@api.route('/api/v1/universal_likes')
class UniversalLikes(Resource):
    """
    Returns all Universal Likes.
    """
    def get(self):
        return jsonify(_get_universal_likes())

def _get_universal_likes():
    url = f'{constants.STARDEW_WIKI}{constants.UNIVERSAL_LIKES}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    universal_likes = character.get_universal_likes(soup)
    return {'universal_likes': universal_likes}

@api.route('/api/v1/list_community_center_rooms')
class ListCommunityCenterRooms(Resource):
    """
    Lists every room in the community center.
    """
    def get(self):
        return jsonify(_list_community_center_rooms())

def _list_community_center_rooms():
    url = f'{constants.STARDEW_WIKI}{constants.BUNDLES}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    room_list = bundles.list_community_center_rooms(soup)
    return {'community_center_rooms': room_list}

@api.route('/api/v1/list_all_bundles')
class ListAllBundles(Resource):
    """
    Lists every bundle in the community center.
    """
    def get(self):
        return jsonify(_list_all_bundles())

def _list_all_bundles():
    url = f'{constants.STARDEW_WIKI}{constants.BUNDLES}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    bundles_list = bundles.list_all_bundles(soup)
    return {'bundles_list': bundles_list}

@api.route('/api/v1/list_bundle_contents')
class ListBundleContents(Resource):
    """
    Lists items from the given bundle.
    """
    def get(self):
        name = request.args.get('name')
        return jsonify(_list_bundle_contents(name))

def _list_bundle_contents(name):
    url = f'{constants.STARDEW_WIKI}{constants.BUNDLES}'
    response = requests.get(url)
    soup = soup_utils.make_soup(response.text)
    bundles_content = bundles.list_bundle_contents(soup, name)
    return {'bundles_content': bundles_content}

@api.route('/api/v1/post_fulfillment')
class PostFulfillment(Resource):
    """
    The fulfillment URL that Google Home hits for queries.
    """
    def post(self):
        data = request.get_json()
        intent = data.get('queryResult').get('action')
        name_param = data.get('queryResult').get('parameters').get('name')

        if intent == 'birthday':
            response = _get_birthday(name_param).get('birthday')
        elif intent == 'best_gifts':
            response = _get_best_gifts(name_param).get('best_gifts')
        elif intent == 'universal_loves':
            response = _get_universal_loves().get('universal_loves')
        elif intent == 'universal_likes':
            response = _get_universal_likes().get('universal_likes')
        elif intent == 'community_center_rooms':
            response = _list_community_center_rooms().get('community_center_rooms')
        elif intent == 'bundles_list':
            response = _list_all_bundles().get('bundles_list')
        elif intent == 'bundles_content':
            response = _list_bundle_contents(name_param).get('bundles_content')

        response_dict = {
            'fulfillmentText': response
        }
        return jsonify(response_dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
