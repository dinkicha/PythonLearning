import math

name_series = input()
episode_time = int(input())
free_time = int(input())

time_for_lunch = free_time * 1/8
time_for_spending = free_time * 1/4
remaining_time = free_time - (time_for_spending + time_for_lunch)

if remaining_time >= episode_time:
    print(f'You have enough time to watch {name_series} and left with {math.ceil(remaining_time - episode_time)}'
          f' minutes free time.')
else:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(episode_time - remaining_time)} "
          f"more minutes.")