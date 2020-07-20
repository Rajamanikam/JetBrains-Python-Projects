# print("""
# Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!
# """)
# print("Write how many cups of coffee you will need: >")
# n = int(input())
# print("For %d cups of coffee you will need: "% n)
# print(200 * n,"ml of water")
# print(50 * n,"ml of milk")
# print(15 * n,"g of coffee beans")
# print("Write how many ml of water the coffee machine has: >")
# water = int(input())
# print("Write how many ml of milk the coffee machine has: >")
# milk = int(input())
# print("Write how many grams of coffee beans the coffee machine has: >")
# beans = int(input())
# print("Write how many cups of coffee you will need: >")
# cups = int(input())

# cup_made_water = water // 200
# cup_made_milk = milk // 50
# cup_made_bean = beans // 15

# cups_made = min(cup_made_water,cup_made_milk,cup_made_bean)

# cup_extra = cups_made - cups

# if cups_made > cups:
#     print('Yes, I can make that amount of coffee (and even',cup_extra,'more than that)')
# elif cups_made == cups :
#     print('Yes, I can make that amount of coffee')
# elif cups_made < cups:
#     print('No, I can make only',cups_made,'cups of coffee')


#print("""
#The coffee machine has:
#400 of water
#540 of milk
#120 of coffee beans
#9 of disposable cups
#550 of money
#""")
class CoffeeMachine():
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.run()
    def action(self, input_text):
         user_input = input(input_text)
         if self.state == "menu":
             return user_input
         elif self.state == "buy":
             if user_input == "back":
                 return user_input
             else:
                 return int(user_input)
         elif self.state == "fill":
             return int(user_input)
     
    def run(self):
        while  True:
            self.state = "menu"
            action = self.action("Write action (buy, fill, take, remaining, exit): >")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break

    def buy(self):
        self.state = "buy"
        choice = self.action("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu : >")
        if choice == "back":
            return None
        elif choice == 1:
            water_cost = 250
            milk_cost = 0
            coffee_beans_cost = 16
            price = 4
        elif choice == 2:
            water_cost = 350
            milk_cost = 75
            coffee_beans_cost = 20
            price = 7
        elif choice == 3:
            water_cost = 200
            milk_cost = 100
            coffee_beans_cost = 12
            price = 6
        else:
            return None
        if self.water >= water_cost and self.milk >= milk_cost and self.coffee_beans >= coffee_beans_cost \
                and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= water_cost
            self.milk -= milk_cost
            self.coffee_beans -= coffee_beans_cost
            self.disposable_cups -= 1
            self.money += price
        else:
            if self.water < water_cost:
                print("Sorry, not enough water!")
            if self.milk < milk_cost:
                print("Sorry, not enough milk!")
            if self.coffee_beans < coffee_beans_cost:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")

    def fill(self):
        self.state = "fill"
        fill_water = self.action("Write how many ml of water do you want to add: ")
        self.water += fill_water
        fill_milk = self.action("Write how many ml of milk do you want to add: ")
        self.milk += fill_milk
        fill_coffee_beans = self.action("Write how many grams of coffee beans do you want to add: ")
        self.coffee_beans += fill_coffee_beans
        fill_disposable_cups = self.action("Write how many disposable cups of coffee do you want to add: ")
        self.disposable_cups += fill_disposable_cups

    def take(self):
        take_money = self.money
        self.money = 0
        print(f"I gave you ${take_money}")

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")


coffee = CoffeeMachine()
