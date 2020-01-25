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

    def get_all_table_ids(self, soup):
        """
        Get all of the tables on a page and their ids.

        :param soup: Beautiful Soup object
        :return: list of table header ids with underscores replaced
        """
        header_id_lists = []

        tables_to_traverse = soup.find_all('table')

        for table in tables_to_traverse:
            first_row = table.find('tr')
            first_th = first_row.find('th')
            if first_th is not None:
                if first_th.has_attr('id'):
                    header_id_lists.append(first_th.attrs['id'].replace("_", " "))
        return header_id_lists

    def get_table_entries(self, soup, table_id):
        """
        Loops through a table looking for nametemplate items and qualitycontainers to grab items in the table.
        :param soup: Beautiful soup object
        :param table_id: the table id
        :return: the list of bundle contents
        """
        table_soup = soup.find(id=table_id).find_parent('tr')
        tr_list = table_soup.find_next_siblings('tr')

        bundle_contents = []
        for row in tr_list:
            # normally, this is a name template
            name_template_sibling = row.find(id='nametemplate')

            # if its a quality item do this
            bundle_quality_sibling = row.find(id='qualitycontainersm')
            if name_template_sibling is not None:
                bundle_link = name_template_sibling.find('a')
                bundle_contents.append(bundle_link.attrs['title'])
            elif bundle_quality_sibling is not None:
                bundle_quality_item = bundle_quality_sibling.find_parent('td')
                bundle_td = bundle_quality_item.find_next_sibling('td')
                # strip out link from td text
                bundle_contents.append(bundle_td.text.strip())

        return bundle_contents

    def list_sections_with_class(self, soup, class_name):
        return soup.find_all(class_=class_name)

    def join_list_human_readable(self, list_to_join):
        return ", ".join(list_to_join[:-2] + [", and ".join(list_to_join[-2:])])