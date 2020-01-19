from souputils import SoupUtils

class Character():
    def get_birthday(self, soup):
        birthday_soup = SoupUtils.get_info_section_by_name(self, soup, 'Birthday:')

        season = birthday_soup.find('a').attrs['title']
        date = birthday_soup.contents[1].strip()
        return f'{season} {date}'