# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return (f'This is {self.name} and it is {self.description}.')

    def add_item(self, item):
        items.append(item)