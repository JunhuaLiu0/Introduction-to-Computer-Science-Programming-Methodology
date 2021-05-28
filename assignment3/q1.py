class flower:
    def __init__(self, name="None", petals=0, price=0.0):
        self.name = name
        self.petals = petals
        self.price = price

    #Input the name of flower
    def give_name(self):
        while True: 
            new_name = input("Please enter the name of flower: ")
            if new_name != "":
                self.name = new_name
                break
            else: print("Please input a correct name.")

    #Input the number of petals of flower
    def give_petals(self):
        while True:
            new_petals = input("Please enter the number of petals of flower: ")
            if new_petals.isdigit():
                self.petals = new_petals
                break
            else:
                print("Please enter a correct number of petals")

    #Input the price of flower
    def give_price(self):
        while True:
            new_price = input("Please enter the price of flower: ")
            FlowerType = type(new_price)
            if FlowerType == float or int:
                self.price = float(new_price)
                break
            else:
                print("Please enter a correct price")


def main():
    input_flower = flower()
    input_flower.give_name()
    input_flower.give_petals()
    input_flower.give_price()
    # Retrieving the value of each type
    print("Name of flower is:", input_flower.name)
    print("Number of petals is:", input_flower.petals)
    print("Price of flower is:", input_flower.price)
main()

