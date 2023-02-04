deposit_sum = float(input())
deposit_months = int(input())
percent = float(input())

percent_gained =  deposit_sum * percent / 100
percent_for_one_month = percent_gained / 12
total_sum = deposit_sum + deposit_months * percent_for_one_month

print(total_sum)

