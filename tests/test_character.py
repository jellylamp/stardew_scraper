import pytest
from bs4 import BeautifulSoup
from src.character import Character

character = Character()

def test_get_birthday_sebastian():
    with open('tests/test_data/sebastian.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    birthday = character.get_birthday(soup)
    assert birthday == 'Winter 10'

def test_get_best_gifts_sebastian():
    with open('tests/test_data/sebastian.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    best_gifts = character.get_best_gifts(soup)
    assert best_gifts == 'Frozen Tear, Obsidian, Pumpkin Soup, Sashimi, and Void Egg'

def test_get_universal_loves():
    with open('tests/test_data/universal_loves.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    loves = character.get_universal_loves(soup)
    assert loves == "The universal loves are: Golden Pumpkin, Magic Rock Candy, Pearl, Prismatic Shard, and Rabbit's" \
        + " Foot. The only exceptions are that Haley hates Prismatic Shard and Penny hates Rabbit's Foot"

def test_get_universal_likes():
    with open('tests/test_data/universal_loves.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    likes = character.get_universal_likes(soup)
    assert likes == "The universal likes are: Artisan Goods, Cooking, Flowers, Minerals, Fruit Trees, Minerals, " \
        + "Vegetables, Life Elixir, and Maple Syrup. For exceptions, see individual characters, universal dislikes," \
        + " and universal hates."
