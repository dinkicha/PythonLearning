count_nylon = int(input())
paint_liters = int(input())
something_for_paint = int(input())
hours_to_finish_the_job = int(input())

price_nylon = (count_nylon + 2) * 1.50
price_paint = (paint_liters * 0.1 + paint_liters) * 14.50
price_something = something_for_paint * 5
price_bag = 0.40
total_price = price_nylon + price_paint + price_something + price_bag
price_workers = total_price * 0.30 * hours_to_finish_the_job
total_price_2 = total_price + price_workers

print(total_price_2)

