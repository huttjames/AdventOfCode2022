
from monkeys import Monkey

M0 = Monkey(0, [52, 60, 85, 69, 75, 75])
M1 = Monkey(1, [96, 82, 61, 99, 82, 84, 85])
M2 = Monkey(2, [95, 79])
M3 = Monkey(3, [88, 50, 82, 65, 77])
M4 = Monkey(4, [66, 90, 59, 90, 87, 63, 53, 88])
M5 = Monkey(5, [92, 75, 62])
M6 = Monkey(6, [94, 86, 76, 67])
M7 = Monkey(7, [57])
Monkeys = [M0, M1, M2, M3, M4, M5, M6, M7]

def printall():
        print("Monkey 0 items: ", Monkeys[0].items)
        print("Monkey 1 items: ", Monkeys[1].items)
        print("Monkey 2 items: ", Monkeys[2].items)
        print("Monkey 3 items: ", Monkeys[3].items)
        print()

def runRound():
    for monkey in Monkeys:
        for i in range(len(monkey.items)):
            monkey.inspectitem()
            recipient = monkey.testitem()
            item = monkey.throw_item()
            Monkeys[recipient].catch_item(item)

for i in range(10000):
    runRound()

handles = []
for monkey in Monkeys:
    handles.append(monkey.counter)

handles.sort()
monkeyBiz = handles[-1] * handles[-2]
print(monkeyBiz)
