from src.souputils import SoupUtils

soup_utils = SoupUtils()

class Character:
    def get_birthday(self, soup):
        birthday_soup = soup_utils.get_info_section_by_name(soup, 'Birthday:')

        season = birthday_soup.find('a').attrs['title']
        date = birthday_soup.contents[1].strip()
        return f'{season} {date}'

    def get_best_gifts(self, soup):
        gift_soup = soup_utils.get_info_section_by_name(soup, 'Best Gifts:')
        gift_list = []

        for gift in gift_soup.find_all('a'):
            gift_list.append(gift.attrs['title'])

        return soup_utils.join_list_human_readable(gift_list)

    def get_universal_loves(self, soup):
        universal_love_id = "Universal_Loves"
        universal_loves = soup_utils.get_header_section_and_lists(soup, universal_love_id, 'h3')
        universal_loves_readable = soup_utils.join_list_human_readable(universal_loves)

        exceptions_id = "Universal_Loves_exceptions"
        universal_loves_exceptions = soup_utils.get_header_section_and_lists(soup, exceptions_id, 'h4')
        readable_exceptions_list = []

        # Parse through exceptions list to make it human readable.
        person = ''
        for count, exception in enumerate(universal_loves_exceptions, start=0):
            # even number
            if count % 2 == 0:
                person = exception
            else:
                hates = exception
                readable_exceptions_list.append(f'{person} hates {hates}')
                # reset now that we have it stored.
                person = ''

        exceptions_readable = soup_utils.join_list_human_readable(readable_exceptions_list)

        description = f'The universal loves are: {universal_loves_readable}. The only exceptions are that {exceptions_readable}'
        return description

    def get_universal_likes(self, soup):
        universal_like_id = "Universal_Likes"
        universal_likes = soup_utils.get_header_section_and_lists(soup, universal_like_id, 'h3', use_all_links=False)
        universal_likes_readable = soup_utils.join_list_human_readable(universal_likes)

        description = f'The universal likes are: {universal_likes_readable}.' +\
                     ' For exceptions, see individual characters, universal dislikes, and universal hates.'
        return description