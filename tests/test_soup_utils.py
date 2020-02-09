import pytest
from bs4 import BeautifulSoup
from src.souputils import SoupUtils

soup_utils = SoupUtils()

def test_was_search_successful_success():
    with open('tests/test_data/sebastian.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    assert soup_utils.was_search_successful(soup) == True

def test_was_search_successful_failure():
    with open('tests/test_data/bad_search.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    assert soup_utils.was_search_successful(soup) == False

def test_get_info_section_by_name_success():
    with open('tests/test_data/sebastian.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    birthday_soup = soup_utils.get_info_section_by_name(soup, 'Birthday:')
    assert birthday_soup is not None

def test_get_info_section_by_name_failure():
    with open('tests/test_data/sebastian.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    birthday_soup = soup_utils.get_info_section_by_name(soup, 'Yo Mama:')
    assert birthday_soup is None

def test_get_header_section_and_lists():
    with open('tests/test_data/universal_loves.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    universal_loves = soup_utils.get_header_section_and_lists(soup, "Universal_Loves", 'h3')
    assert 'Prismatic Shard' in universal_loves

def test_get_header_section_and_lists_only_first_link():
    with open('tests/test_data/universal_loves.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    universal_likes = soup_utils.get_header_section_and_lists(soup, "Universal_Likes", 'h3', use_all_links=False)
    assert 'Cooking' in universal_likes

def test_get_all_table_ids():
    with open('tests/test_data/bundles.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    table_ids = soup_utils.get_all_table_ids(soup)
    assert 'Construction Bundle' in table_ids

@pytest.mark.skip(reason="Failing after SDV update")
def test_get_table_entries_constuction():
    with open('tests/test_data/bundles.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    bundle_items = soup_utils.get_table_entries(soup, 'Construction_Bundle')
    assert 'wood' in bundle_items

def test_list_sections_with_class():
    with open('tests/test_data/bundles.html') as html:
        soup = BeautifulSoup(html, 'html.parser')
    room_soup = soup_utils.list_sections_with_class(soup, 'mw-headline')
    assert room_soup is not None

def test_join_list_human_readable_three_items():
    test_list = ['Snap', 'Crackle', 'Pop']
    assert soup_utils.join_list_human_readable(test_list) == 'Snap, Crackle, and Pop'

def test_join_list_human_readable_two_items():
    test_list = ['Snap', 'Crackle']
    assert soup_utils.join_list_human_readable(test_list) == 'Snap and Crackle'