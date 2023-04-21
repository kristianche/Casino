from SlotMachines.SlotMachines import SlotMachine
import random


class Numbers(SlotMachine):

    icons = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    reels_dict = {}

    def __init__(self, money: float):
        self._money = money

    @staticmethod
    def rules():
        return "Here are the icons of which 5 will be generated for you: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9  \n" \
               "If you have 3 icons which match the money you have bet are increased by 300 dollars. \n" \
               "If you have 4 icons which match the money you have bet are increased by 400 dollars.. \n" \
               "If you have 5 icons which match the money you have bet are increased by 500 dollars. "

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

        reels = [random.choice(Numbers.icons) for _ in range(5)]

        for number in reels:
            if number in Numbers.reels_dict:
                Numbers.reels_dict[number] += 1
            else:
                Numbers.reels_dict[number] = 1

        print(f"{' '.join(reels)}")

        for key in Numbers.reels_dict:
            if Numbers.reels_dict[key] == 3:
                winnings = 300 + bet_money
                self._money += winnings
                print(f"You won 300 dollars and your amount now is {self._money}")
                break
            elif Numbers.reels_dict[key] == 4:
                winnings = 400 + bet_money
                self._money += winnings
                print(f"You won 400 dollars and your amount now is {self._money}")
                break
            elif Numbers.reels_dict[key] == 5:
                winnings = 500 + bet_money
                self._money += winnings
                print(f"You won 500 dollars and your amount now is {self._money}")
                break
        else:
            self._money -= bet_money
            print(f"Sorry! You lost {bet_money} and your amount now is {self._money}")


        Numbers.reels_dict = {}
        print()


