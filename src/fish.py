from souputils import SoupUtils

class Fish():
    def get_fish_info(self, soup):
        fish_found_in_soup = SoupUtils.get_info_section_by_name(self, soup, 'Found in:')
        fish_found_in_string = self._handle_link_or_string(fish_found_in_soup)

        fish_time_found_soup = SoupUtils.get_info_section_by_name(self, soup, 'Time:')
        fish_time_contents = self._handle_link_or_string(fish_time_found_soup)
        if fish_time_contents == 'Any':
            fish_time_contents = f'{fish_time_contents} time'

        fish_season_soup = SoupUtils.get_info_section_by_name(self, soup, 'Season:')
        fish_season_contents = self._handle_link_or_string(fish_season_soup)
        if fish_season_contents == 'All':
            fish_season_contents = f'{fish_season_contents} seasons'

        fish_weather_soup = SoupUtils.get_info_section_by_name(self, soup, 'Weather:')
        fish_weather_contents = self._handle_link_or_string(fish_weather_soup)
        if fish_weather_contents == 'Any':
            fish_weather_contents = f'{fish_weather_contents} weather'

        fish_info_string = f'Can be found in the {fish_found_in_string} at {fish_time_contents}' \
            f' in {fish_season_contents} in {fish_weather_contents}.'

        return fish_info_string

    def _handle_link_or_string(self, soup):
        contents_list = []
        if soup.find_all('a'):
            contents = soup.find_all('a')
            contents_list.append([fish.get_text() for fish in contents if fish.get_text() != ''])
        if soup.contents:
            contents_list.append(soup.contents[0].strip())
        print("contents_list", contents_list)
        contents = SoupUtils.join_list_human_readable(self, contents_list)
        return contents