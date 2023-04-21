from SlotMachines.SlotMachines import SlotMachine
from SlotMachines.Numbers import Numbers
from SlotMachines.Lucky7 import Lucky7
from SlotMachines.HappyFruits import HappyFruits
import time


class Casino:

    def __init__(self):
        self.game = ""

    def rules_and_types_of_games(self):

            return_string = "Here in BCF Casino there are 3 types of slot machine games: Lucky 7, Numbers, Happy Fruits"
            return f"{return_string}\n" \
                   f"Lucky 7 rules: \n" \
                   f"{Lucky7.rules()} \n" \
                   f"Numbers rules: \n" \
                   f"{Numbers.rules()} \n" \
                   f"Happy Fruits rules: \n" \
                   f"{HappyFruits.rules()} "

    def slot_machine_game_choice(self, choice, money):
        if choice == "L":
            self.game = Lucky7(money)
            return f"You chose to play Lucky 7 with starting amount: {money} dollars!"
        elif choice == "N":
            self.game = Numbers(money)
            return f"You chose to play Numbers with starting amount: {money} dollars!"
        elif choice == "H":
            self.game = HappyFruits(money)
            return f"You chose to play Happy Fruits with starting amount: {money} dollars!"

    def play(self):
        if isinstance(self.game, Lucky7):
            self.game.play()
        elif isinstance(self.game, Numbers):
            self.game.play()
        elif isinstance(self.game, HappyFruits):
            self.game.play()


print("Hello and welcome to BCF Casino!")
print("Here you can play on slot machines or play cards games.")
casino = Casino()
print(casino.rules_and_types_of_games())
slot_game_choice = input("Now! Choose your game(L - Lucky 7, N - Numbers, H - Happy Fruits): ")
if slot_game_choice != "N" and slot_game_choice != "L" and slot_game_choice != "H":
    raise ValueError("Please choose game from the valid ones!")
money = int(input("Now! Insert your starting money: "))
print(casino.slot_machine_game_choice(slot_game_choice, money))
while True:
    casino.play()
