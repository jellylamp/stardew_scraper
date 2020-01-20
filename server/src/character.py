from souputils import SoupUtils

class Character():
    def get_birthday(self, soup):
        birthday_soup = SoupUtils.get_info_section_by_name(self, soup, 'Birthday:')

        season = birthday_soup.find('a').attrs['title']
        date = birthday_soup.contents[1].strip()
        return f'{season} {date}'

    def get_best_gifts(self, soup):
        gift_soup = SoupUtils.get_info_section_by_name(self, soup, 'Best Gifts:')
        gift_list = []

        for gift in gift_soup.find_all('a'):
            gift_list.append(gift.attrs['title'])

        return ", ".join(gift_list[:-2] + [", and ".join(gift_list[-2:])])