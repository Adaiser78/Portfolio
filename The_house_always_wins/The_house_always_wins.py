import random
random.seed(5)
spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
          18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
          33, 34, 35, 36]

profit_goal = int(input("Profit Goal: "))
starting_money = int(input("Starting money: "))
table_minimum_bet = int(input("Table minimum bet: "))
table_maximum_bet = int(input("Table maximum bet: "))
print(f"Starting Money: {starting_money}")
enough_money = True
win_spin = False
bet = table_minimum_bet
profit = False
previous_money = starting_money


while enough_money and not profit:
    spin = random.choice(spaces)

    if spin % 2 != 0:
        win_spin = True

    if win_spin:
        total = previous_money + bet
        print(f"Spin: {spin}. You won ${bet} on the bet. "
              f"You had {previous_money}. Now you have {total} left.")
        bet = table_minimum_bet
    else:
        total = previous_money - bet
        print(f"Spin: {spin}. You lost ${bet} on the bet. "
              f"You had {previous_money}. Now you have {total} left.")
        if bet*2 <= table_maximum_bet and total >= bet*2:
            bet *= 2
        else:
            bet = table_minimum_bet

    if total < bet:

        enough_money = False
    if total >= profit_goal:
        profit = True

    win_spin = False
    previous_money = total


if profit:
    print(f"You reached your goal and beat the casino. You should stop now. "
          f"You have ${total}.")
else:
    print("You ran out of money")

