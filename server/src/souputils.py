from bs4 import BeautifulSoup

class SoupUtils():
    def make_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def was_search_successful(self, response_soup):
        class_found = response_soup.find(class_='mw-search-createlink')
        if class_found is None:
            return True
        return False

    def get_info_table(self, soup):
        return soup.find(id='infoboxtable')

    def get_info_section_by_name(self, soup, name):
        info_table = SoupUtils.get_info_table(self, soup)

        info_box_sections = info_table.find_all(id='infoboxsection')
        for box_section in info_box_sections:
            if box_section.text.strip() == name:
                parent_tr = box_section.find_parent('tr')
                details = parent_tr.find(id='infoboxdetail')
                return details

    def get_header_section_and_lists(self, soup, header_id, header_parent, use_all_links=True):
        """
        Get the header section with the provided id and all of the list items under it.

        :param soup: Beautiful Soup object
        :param header_id: the header id
        :param header_parent: the header wrapper (i.e. h4)
        :param use_all_links: defaults to true. If passed in false, will not grab all the items
               in a list item, only the first.
        :return: list of items
        """
        header = soup.find(id=header_id).find_parent(header_parent)
        list_items = []

        sibling = header.find_next_sibling("ul")
        list_items_to_traverse = sibling.find_all('li')
        for item in list_items_to_traverse:
            if use_all_links:
                item_links = item.find_all('a')
                for link in item_links:
                    list_items.append(link.attrs['title'])
            else:
                list_items.append(item.find('a').attrs['title'])

        return list_items

    def list_sections_with_class(self, soup, class_name):
        return soup.find_all(class_=class_name)

    def join_list_human_readable(self, list_to_join):
        return ", ".join(list_to_join[:-2] + [", and ".join(list_to_join[-2:])])