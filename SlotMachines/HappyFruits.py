from SlotMachines.SlotMachines import SlotMachine
import random


class HappyFruits(SlotMachine):

    icons = ["banana", "apple", "orange", "strawberry"]
    reels_dict = {}

    def __init__(self, money: float):
        self._money = money

    @staticmethod
    def rules():
        return "Here are the icons of which 4 will be generated for you: (fruits list) \n" \
               "If you have 3 icons which match the money you have bet are increased by 300 dollars. \n" \
               "If you have 4 icons which match the money you have bet are increased by 600 dollars."

    def play(self):
        if self._money <= 0:
            print("You ran out of money!")
            return

        while True:
            try:
                bet_money = int(input("Place your bet money: "))
                if bet_money <= 0 or bet_money > self._money:
                    raise ValueError
                break
            except ValueError:
                print(f"Please insert a number between 1 and {self._money}")

        reels = [random.choice(HappyFruits.icons) for _ in range(4)]

        for fruit in reels:
            if fruit in HappyFruits.reels_dict:
                HappyFruits.reels_dict[fruit] += 1
            else:
                HappyFruits.reels_dict[fruit] = 1

        print(f"{' '.join(reels)}")

        for key in HappyFruits.reels_dict:
            if HappyFruits.reels_dict[key] == 3:
                winnings = 300 + bet_money
                self._money += winnings
                print(f"You won 300 dollars and your amount now is {self._money}")
                break
            elif HappyFruits.reels_dict[key] == 4:
                winnings = 600 + bet_money
                self._money += winnings
                print(f"You won 600 dollars and your amount now is {self._money}")
                break
        else:
            self._money -= bet_money
            print(f"Sorry! You lost {bet_money} and your amount now is {self._money}")

        HappyFruits.reels_dict = {}
        print()