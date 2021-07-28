from src.souputils import SoupUtils
from bs4 import BeautifulSoup

soup_utils = SoupUtils()

class Fish:
    def get_fish_info(self, soup):
        fish_found_in_soup = soup_utils.get_info_section_by_name(soup, 'Found in:')
        fish_found_in_string = self._handle_link_or_string(fish_found_in_soup)

        fish_time_found_soup = soup_utils.get_info_section_by_name(soup, 'Time:')
        fish_time_contents = self._handle_link_or_string(fish_time_found_soup)
        if fish_time_contents == 'Any':
            fish_time_contents = f'{fish_time_contents} time'

        fish_season_soup = soup_utils.get_info_section_by_name(soup, 'Season:')
        fish_season_contents = self._handle_link_or_string(fish_season_soup)
        if fish_season_contents == 'All':
            fish_season_contents = f'{fish_season_contents} seasons'

        fish_weather_soup = soup_utils.get_info_section_by_name(soup, 'Weather:')
        fish_weather_contents = self._handle_link_or_string(fish_weather_soup)
        if fish_weather_contents == 'Any':
            fish_weather_contents = f'{fish_weather_contents} weather'

        fish_info_string = f'Can be found in the {fish_found_in_string} at {fish_time_contents}' \
            f' in {fish_season_contents} in {fish_weather_contents}.'

        return fish_info_string

    def _handle_link_or_string(self, soup):
        contents_list = []
        # TODO look for bullet as a separator and string those words together

        string_builder = []
        for item in soup.contents:
            item_soup = BeautifulSoup(str(item), 'html.parser')
            if item_soup.find_all('a'):
                [string_builder.append(contents.get_text()) for contents in item_soup.find_all('a') if contents.get_text() != '']
            else:
                if item_soup.contents[0]:
                    # skip images
                    img_soup = BeautifulSoup(str(item_soup), 'html.parser')
                    if img_soup.find('img'):
                        continue

                    # We have found a word separator. add string builder to contents_list joined.
                    if '•' in item_soup.contents[0]:
                        contents_list.append(' '.join(string_builder))
                        string_builder = []

                    # strip out special characters
                    contents = item_soup.contents[0].replace('•', '').replace('–', 'to').replace('-', 'to').strip()
                    if contents != '':
                        string_builder.append(contents)

        # if there was only one option and there is no word separator bullet
        if len(string_builder) != 0:
            contents_list.append(' '.join(string_builder))

        contents = soup_utils.join_list_human_readable(contents_list)
        return contents