import random


class ecosystem:
    def __init__(self, river=[], fish=0, bear=0, step=0):
        self.fish = fish
        self.bear = bear
        self.river = river

    # Input the number of fish
    def setFish(self):
        while True:
            set_fish = input("How many fishes?:")
            if set_fish.isdigit():
                self.fish = int(set_fish)
                break
            else:
                print("Please enter a correct number")

    # Input the number of bear
    def setBear(self):
        while True:
            set_bear = input("How many bears?:")
            if set_bear.isdigit():
                self.bear = int(set_bear)
                break
            else:
                print("Please enter a correct number")

    # Initialize the river and generate a river with bear and fish.
    def initialRiver(self):
        while True:
            set_len = input("How long is the river?:")
            if set_len.isdigit() and int(set_len) >= self.bear + self.fish:
                set_len = int(set_len)
                break
            else:
                print("Please enter a correct number")
        # Fill the river with bears and fish randomly.
        self.river = []
        position_list = list(range(set_len))
        for i in range(set_len):
            self.river.append("N")
        fish_list = random.sample(position_list, self.fish)
        for i in fish_list:
            self.river[i] = "F"
            position_list.remove(i)
        bear_list = random.sample(position_list, self.bear)
        for i in bear_list:
            self.river[i] = "B"

    # The animals from left to right move one by one and execute several times according to the number of steps.
    def simulation(self):
        while True:
            n = input("How many steps do you want?:")
            if n.isdigit() and int(n) > 0:
                n = int(n)
                break
            else:
                print("Please enter a correct number")
        total_round = 0
        break_all = False
        kill_forward_animal = False
        while total_round < n:
            middle_list = [-1, 0, 1]
            left_list = [0, 1]
            right_list = [-1, 0]
            # Define several list to record the position of each type
            animal_list = []
            none_list = []
            baby_list = []
            count = 0
            for i in self.river:
                if i == "B" or i == "F":
                    animal_list.append(count)
                if i == "N":
                    none_list.append(count)
                count = count + 1
            for i in animal_list:
                if kill_forward_animal == False:
                    # Each position has different choices to move
                    if i == 0:
                        move = random.sample(left_list, 1)[0]
                    if i == len(self.river) - 1:
                        move = random.sample(right_list, 1)[0]
                    else:
                        move = random.sample(middle_list, 1)[0]
                    if self.river[i] == "F" and move != 0:
                        if self.river[i + move] == "N":
                            self.river[i + move] = "F"
                            self.river[i] = "N"
                            none_list.append(i)
                            animal_list.remove(i)
                            none_list.remove(i + move)
                            animal_list.append(i + move)
                        if self.river[i + move] == "B":
                            self.river[i] = "N"
                            none_list.append(i)
                        if self.river[i + move] == "F":
                            baby_list.append("F")
                    if self.river[i] == "B" and move != 0:
                        if self.river[i + move] == "N":
                            self.river[i + move] = "B"
                            self.river[i] = "N"
                            animal_list.remove(i)
                            none_list.remove(i + move)
                            none_list.append(i)
                            animal_list.append(i + move)
                        if self.river[i + move] == "F":
                            self.river[i + move] = "B"
                            self.river[i] = "N"
                            none_list.append(i)
                            if (
                                move == 1
                            ):  # Make sure each animal only move one times each round
                                kill_forward_animal = True
                        if self.river[i + move] == "B":
                            baby_list.append("B")
                if kill_forward_animal:
                    kill_forward_animal = False
            # Baby will not join the river immediately, but will fill the empty place in the next round.
            if len(baby_list) > 0:
                for baby in baby_list:
                    if len(none_list) != 0:
                        new_baby_fish = random.sample(none_list, 1)[0]
                        self.river[new_baby_fish] = baby
                        none_list.remove(new_baby_fish)
            # When the river is full and all animals are fish or bears, the step ends in advance.
            if (len(set(self.river)) == 1) and (len(none_list) == 0):
                print("The river is full.")
                break
            total_round = total_round + 1


BearFish = ecosystem()
BearFish.setFish()
BearFish.setBear()
BearFish.initialRiver()
print(BearFish.river)
BearFish.simulation()
print(BearFish.river)
