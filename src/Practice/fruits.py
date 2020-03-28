#Fruits shop
# Fruits - display fruits available, sell the fruits
#Customer - request to order fruits


class Fruits:

    def __init__(self, fruitsList):
        self.availableFruits = fruitsList

    def displayFruits(self):
        print()
        print("Fruits available")
        for fruit in self.availableFruits:
            print(fruit)


    def sellFruits(self, orderedFruits):
        if orderedFruits in self.availableFruits:
            print("You have successfully ordered the fruits")
            self.availableFruits.remove(orderedFruit)
        else:
            print("Sorry! The fruits that you are ordering is sold out. Thank you!")

class Customer:

    def orderFruits(self):
        print("Enter the name of the fruit would you like to buy ")
        self.fruit=input()
        return self.fruit


fruits = Fruits(['Apple','Banana','Papaya','Strawberry'])


customer = Customer()
while True:
    print("Enter 1 to display the available fruits")
    print("Enter 2 to order fruit")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        fruits.displayFruits()
    elif userChoice is 2:
        orderedFruit = customer.orderFruits()
        fruits.sellFruits((orderedFruit))
    elif userChoice is 3:
        quit()