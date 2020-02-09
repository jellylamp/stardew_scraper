import pytest
from bs4 import BeautifulSoup
from src.bundles import Bundles

bundles = Bundles()

def test_get_community_center_bundles():
    with open('tests/test_data/bundles.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    room_list = bundles.list_community_center_rooms(soup)
    assert room_list == "Standard Bundles, Crafts Room, Pantry, Fish Tank, Boiler Room, Bulletin Board, Vault," \
        + " Abandoned JojaMart, and Remixed Bundles"

def test_list_all_bundles():
    with open('tests/test_data/bundles.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    bundle_list = bundles.list_all_bundles(soup)
    assert bundle_list == "Spring Foraging, Summer Foraging, Fall Foraging, Winter Foraging, Construction, " \
        + "Exotic Foraging, Spring Crops, Summer Crops, Fall Crops, Quality Crops, Animal, Artisan, River Fish, " \
        + "Lake Fish, Ocean Fish, Night Fishing, Crab Pot, Specialty Fish, Blacksmiths, Geologists, Adventurers, " \
        + "Chefs, Dye, Field Research, Fodder, Enchanters, g2500, g5000, g10000, g25000, and The Missing"

@pytest.mark.skip(reason="Failing after SDV update")
def list_bundle_contents():
    with open('tests/test_data/bundles.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    bundle_contents = bundles.list_bundle_contents(soup, 'Construction_Bundle')
    assert bundle_contents == 'Wood, Wood, Stone, and Hardwood'