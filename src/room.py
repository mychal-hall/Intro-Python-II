# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        output = f'{self.name}: {self.description}'
        return output

    def list_items(self):
        if len(self.items) == 0:
            return f'there are no items here.'
        else:
            return f'there are {self.items} here.'