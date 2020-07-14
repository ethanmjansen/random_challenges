class towers_of_hanoi():
    def __init__(self):
        self.tower_1 = []
        self.tower_2 = []
        self.tower_3 = []


    def __str__(self):
        return f'Tower 1: {self.tower_1}\nTower 2: {self.tower_2}\nTower 3: {self.tower_3}'


    def add_to_tower(self, tower, value):
        if tower == self.tower_1:
            self.tower_1.append(value)
        elif tower == self.tower_2:
            self.tower_2.append(value)
        else:
            self.tower_3.append(value)

    def move_value(self, origin, destination):
        if origin == destination:
            print('\norigin and destination are the same')

        if origin == self.tower_1:
            value = self.tower_1.pop()
        elif origin == self.tower_2:
            value == self.tower_2.pop()
        else:
            value == self.tower_3.pop()

        if destination == self.tower_1:
            self.tower_1.append(value)
        elif destination == self.tower_2:
            self.tower_2.append(value)
        else:
            self.tower_3.append(value)

if __name__ == '__main__':

    towers = towers_of_hanoi()

    for i in range(1, 4):
        towers.add_to_tower(towers.tower_1, i)

    print(towers)
    towers.move_value(towers.tower_1, towers.tower_2)
    print(f'\n{towers}')



