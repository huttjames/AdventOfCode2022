import math

# This is for 8 monkeys

# This is the product of all the prime factors carried out in the tests
bigprime = 13*7*19*2*5*3*11*17

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
            if item % 13 == 0:
                return 6
            else:
                return 7
        if self.id == 1:
            if item % 7 == 0:
                return 0
            else:
                return 7
        if self.id == 2:
            if item % 19 == 0:
                return 5
            else:
                return 3
        if self.id == 3:
            if item % 2 == 0:
                return 4
            else:
                return 1
        if self.id == 4:
            if item % 5 == 0:
                return 1
            else:
                return 0
        if self.id == 5:
            if item % 3 == 0:
                return 3
            else:
                return 4
        if self.id == 6:
            if item % 11 == 0:
                return 5
            else:
                return 2
        if self.id == 7:
            if item % 17 == 0:
                return 6
            else:
                return 2

    def inspectitem(self):
        item = self.items[0]
        self.counter += 1

        if self.id == 0:
            newitemworry = item * 17
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 1:
            newitemworry = item + 8
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 2:
            newitemworry = item + 6
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 3:
            newitemworry = item * 19
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 4:
            newitemworry = item + 7
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 5:
            newitemworry = item * item
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 6:
            newitemworry = item + 1
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry
        if self.id == 7:
            newitemworry = item + 2
            newitemworry = newitemworry % bigprime
            # newitemworry = math.floor(newitemworry / 3)
            self.items[0] = newitemworry
            return newitemworry







