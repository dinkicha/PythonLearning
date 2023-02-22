import math
budget_movie = float(input())
count_statistics = int(input())
price_clothes_for_one = float(input())

price_decor = budget_movie * 0.10
price_clothes = count_statistics * price_clothes_for_one

if count_statistics > 150:
    price_clothes2 = price_clothes * 0.10
    price_clothes = price_clothes - price_clothes2

total_sum = price_decor + price_clothes
diff = abs(budget_movie - total_sum)

if budget_movie >= total_sum:
    print(f'Action! '
          f'\nWingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money! '
          f'\nWingard needs {diff:.2f} leva more.')