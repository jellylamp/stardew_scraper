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
