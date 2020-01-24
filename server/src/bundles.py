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