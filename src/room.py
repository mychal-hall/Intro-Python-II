# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        output = f'{self.name}: {self.description}'
        return output

    def list_items(self):
        if len(self.items) == 0:
            return f'there are no items here.'
        elif len(self.items) == 1:
            return f'there is a {self.items} here.'
        elif len(self.items) >= 2:
            return f'there are {self.items} here'
