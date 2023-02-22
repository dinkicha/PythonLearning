import math

peter_budget = float(input())
count_video_cards = int(input())
count_processors = int(input())
count_ram = int(input())

price_video_cards = count_video_cards * 250
price_processor = price_video_cards * 0.35
price_ram = price_video_cards * 0.10

total_sum_cpu = count_processors * price_processor
total_sum_ram = count_ram * price_ram

total_sum = price_video_cards + total_sum_cpu + total_sum_ram

if count_video_cards > count_processors:
    total_sum = total_sum - (total_sum * 0.15)

diff = abs(total_sum - peter_budget)


if peter_budget >= total_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
