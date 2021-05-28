class listStack:
    def __init__(self):
        self.data = list()

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

def HanoiTower(n):
    Situation = listStack()
    Situation.push(list())
    for i in range(n):
        step_list = Situation.pop()
        if (i % 2 == 0 and n % 2 == 0) or (i % 2 != 0 and n % 2 != 0):
            transfer_step_list = list()
            for j in step_list:
                transfer_step_list.append(situation1(j))
            step_list.append("A --> B")
            step_list += transfer_step_list
        else:
            transfer_step_list = list()
            for j in step_list:
                transfer_step_list.append(situation2(j))
            step_list.append("A --> C")
            step_list += transfer_step_list
        Situation.push(step_list)
    for i in step_list:
        print(i)

def situation2(n):
    sequence_list = list(n)
    new_list = list()
    for i in sequence_list:
        if i == "A":
            i = "B"
        elif i == "B":
            i = "C"
        elif i == "C":
            i = "A"
        new_list.append(i)
    new_step_list = "".join(new_list)
    return new_step_list


def situation1(n):
    sequence_list = list(n)
    new_list = list()
    for i in sequence_list:
        if i == "A":
            i = "C"
        elif i == "B":
            i = "A"
        elif i == "C":
            i = "B"
        new_list.append(i)
    new_step_list = "".join(new_list)
    return new_step_list


def main():
    print("Welcome to the Hanoi tower")
    while True:
        try:
            n = int(input("Please input the number of disks(a positive integer): "))
            break
        except:
            print("Please enter a proper positive number")
    HanoiTower(n)


main()
