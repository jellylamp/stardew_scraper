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

        return SoupUtils.join_list_human_readable(self, gift_list)

    def get_universal_loves(self, soup):
        universal_love_id = "Universal_Loves"
        universal_loves = SoupUtils.get_header_section_and_lists(self, soup, universal_love_id, 'h3')
        universal_loves_readable = SoupUtils.join_list_human_readable(self, universal_loves)

        exceptions_id = "Universal_Loves_exceptions"
        universal_loves_exceptions = SoupUtils.get_header_section_and_lists(self, soup, exceptions_id, 'h4')
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

        exceptions_readable = SoupUtils.join_list_human_readable(self, readable_exceptions_list)

        description = f'The universal loves are: {universal_loves_readable}. The only exceptions are that {exceptions_readable}'
        return description

    def get_universal_likes(self, soup):
        universal_like_id = "Universal_Likes"
        universal_likes = SoupUtils.get_header_section_and_lists(self, soup, universal_like_id, 'h3', use_all_links=False)
        universal_likes_readable = SoupUtils.join_list_human_readable(self, universal_likes)

        description = f'The universal likes are: {universal_likes_readable}.' +\
                     ' For exceptions, see individual characters, universal dislikes, and universal hates.'
        return description