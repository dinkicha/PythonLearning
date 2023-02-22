import math
price_vacation = float(input())
count_puzzles = float(input())
count_talking_dolls = int(input())
count_teddy_bear = int(input())
count_minions = int(input())
count_trucks = int(input())

price = count_puzzles * 2.60 + count_talking_dolls * 3 + \
        count_teddy_bear * 4.10 + count_minions * 8.20 + count_trucks * 2

count_everything = count_puzzles + count_trucks + count_minions + count_talking_dolls + count_teddy_bear

if count_everything >= 50:
    price = price * 0.75

price = price * 0.90

diff = abs(price - price_vacation)

if price >= price_vacation:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
