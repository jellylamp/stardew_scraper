from souputils import SoupUtils

class Bundles():
    def list_community_center_rooms(self, soup):
        room_soup = SoupUtils.list_sections_with_class(self, soup, 'mw-headline')
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
        return SoupUtils.join_list_human_readable(self, room_list)

    def list_all_bundles(self, soup):
        bundle_id_list = SoupUtils.get_all_table_ids(self, soup)
        # remove bundle from every entry
        list_without_bundle = [text.rsplit(' ', 1)[0] for text in bundle_id_list]

        return SoupUtils.join_list_human_readable(self, list_without_bundle)

    def list_bundle_contents(self, soup, name):
        content_list = SoupUtils.get_table_entries(self, soup, name)
        return SoupUtils.join_list_human_readable(self, content_list[:-1])