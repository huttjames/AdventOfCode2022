# This is for 4 monkeys

import math
bigprime = 23 * 19 * 13 * 17

class Monkey:
    def __init__(self, id, items, counter=0):
        self.id = id
        self.items = items
        self.counter = counter

    def catch_item(self, item):
        newitems = self.items + [item]
        self.items = newitems
        return newitems

    def throw_item(self):
        item = self.items[0]
        newitems = self.items[1:]
        self.items = newitems
        return item


    def testitem(self):
        item = self.items[0]
        if self.id == 0:
            if item % 23 == 0:
                return 2
            else:
                return 3
        if self.id == 1:
            if item % 19 == 0:
                return 2
            else:
                return 0
        if self.id == 2:
            if item % 13 == 0:
                return 1
            else:
                return 3
        if self.id == 3:
            if item % 17 == 0:
                return 0
            else:
                return 1

    def inspectitem(self):
        item = self.items[0]
        self.counter += 1

        if self.id == 0:
            newitemworry = item * 19
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 1:
            newitemworry = item + 6
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 2:
            newitemworry = item * item
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 3:
            newitemworry = item + 3
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
 




