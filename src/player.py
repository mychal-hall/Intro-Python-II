# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __repr__(self):
        return repr(self.name)

    def get_item(self):
        if self.current_room.items:
            return f'there are {self.current_room.items} here.'
