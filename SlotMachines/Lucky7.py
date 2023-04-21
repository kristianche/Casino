from SlotMachines.SlotMachines import SlotMachine
import random


class Lucky7(SlotMachine):

    icons = ["7", ":)", ":(", ":|"]

    def __init__(self, money: float,):
        self._money = money

    @staticmethod
    def rules():
        return "Here are the icons of which 3 will be generated for you: 7, :), :(, :| \n" \
               "If you have 2 icons which match your bet money are multiplied by 2. \n" \
               "If you have 3 icons which match your bet money are multiplied by 3. \n" \
               "If you have 3 seven your bet money are multiplied by 7."

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

        reels = [random.choice(Lucky7.icons) for _ in range(3)]

        if reels[0] == reels[1] == reels[2]:
            print(f"{' '.join([str(i) for i in reels])}")
            winnings = bet_money * 3
            self._money += winnings
            print(f"JACKPOT! You won {winnings} dollars and your amount of money now is {self._money}.")
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            print(f"{' '.join([str(i) for i in reels])}")
            winnings = bet_money * 2
            self._money += winnings
            print(f"You won {winnings} dollars and your amount of money now is {self._money}.")
        elif reels[0] == reels[1] == reels[2] == "7":
            print(f"{' '.join([str(i) for i in reels])}")
            winnings = bet_money * 7
            self._money += winnings
            print(f"JACKPOT! You won {winnings} dollars and your amount of money now is {self._money}.")
        else:
            print(f"{' '.join([str(i) for i in reels])}")
            self._money -= bet_money
            print(f"Sorry! You lost {bet_money} and your amount of money now is {self._money}.")

        print()



