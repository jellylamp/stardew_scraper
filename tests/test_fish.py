import pytest
from bs4 import BeautifulSoup
from src.fish import Fish

fish = Fish()

def test_get_fish_info_pufferfish_one_season_specific_time():
    """This is a simple example with a specific times and weather and only one season it can be found."""
    with open('tests/test_data/pufferfish.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    assert fish_output == 'Can be found in the Ocean at 12pm to 4pm in Summer in Sun.'

def test_get_fish_info_anchovy():
    """This example has multiple seasons and says Any for both weather and time. """
    with open('tests/test_data/anchovy.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    assert fish_output == 'Can be found in the Ocean at Any time in Spring and Fall in Any weather.'

def test_get_fish_info_tuna():
    """This example has multiple seasons and says Any for weather and has a specific time. """
    with open('tests/test_data/tuna.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    assert fish_output == 'Can be found in the Ocean at 6am to 7pm in Summer and Winter in Any weather.'

def test_get_fish_info_bream():
    """This example has All for seasons and says Any for weather and has a specific time. """
    with open('tests/test_data/bream.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    assert fish_output == 'Can be found in the River at 6pm to 2am in All seasons in Any weather.'

@pytest.mark.skip(reason="Failing after SDV update")
def test_get_fish_info_smallmouth_bass():
    """This example has multiple seasons, says Any for weather, has multiple locations (including town river)
     and at any time. """
    with open('tests/test_data/smallmouth_bass.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    # TODO make these commas less whack
    assert fish_output == 'Can be found in the Town River, and Forest Pond at Any time in Spring and Fall in Any weather.'

@pytest.mark.skip(reason="Failing after SDV update")
def test_get_fish_info_walleye():
    """This example has multiple seasons, says Any for weather, has multiple locations (including town river)
     and at any time. """
    with open('tests/test_data/walleye.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    # TODO make these commas less whack
    assert fish_output == 'Can be found in the River, Mountain Lake, Forest, Pond, Forest Farm, and Pond at 12pm to 2am in Fall, Winter, with, and Rain Totem in Rain.'

@pytest.mark.skip(reason="Failing after SDV update")
def test_get_fish_info_catfish():
    """This example has multiple seasons in different locations, only available in the rain, has multiple locations.
     and at any time. """
    # TODO make this test not whack
    with open('tests/test_data/catfish.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    fish_output = fish.get_fish_info(soup)
    assert fish_output == "Can be found in the River, Secret Woods, and Witch's Swamp at 6am to 12am in Spring, Fall," \
            " Secret Woods, Witch's Swamp, Spring, Summer, and Fall in Rain."

