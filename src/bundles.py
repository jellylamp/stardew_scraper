from src.souputils import SoupUtils

soup_utils = SoupUtils()

class Bundles():
    def list_community_center_rooms(self, soup):
        room_soup = soup_utils.list_sections_with_class(soup, 'mw-headline')
        room_list = []
        items_to_exclude = [
            'Traveling Cart Availability',
            'Bugs',
            'History'
        ]

        # loop through rooms and add titles to the list
        for room in room_soup:
            text_to_add = room.text
            if text_to_add not in items_to_exclude:
                room_list.append(room.text)
        return soup_utils.join_list_human_readable(room_list)

    def list_all_bundles(self, soup):
        bundle_id_list = soup_utils.get_all_table_ids(soup)
        # remove bundle from every entry
        list_without_bundle = [text.rsplit(' ', 1)[0] for text in bundle_id_list]

        return soup_utils.join_list_human_readable(list_without_bundle)

    def list_bundle_contents(self, soup, name):
        content_list = soup_utils.get_table_entries(soup, name)
        return soup_utils.join_list_human_readable(content_list[:-1])