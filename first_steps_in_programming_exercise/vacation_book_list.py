import math
pages = int(input())
pages_for_one_hour = int(input())
days = int(input())

hours_total = pages / pages_for_one_hour
hours_total = hours_total / days
down = math.floor(hours_total)
print(down)
