count_chicken = int(input())
count_fish = int(input())
count_vegeterian = int(input())

price_chicken = count_chicken * 10.35
price_fish = count_fish * 12.40
price_vegeterian = count_vegeterian * 8.15
total_price = price_fish + price_vegeterian + price_chicken

price_dessert = total_price * 0.20
price_delivery = 2.50

total_delivery = total_price + price_dessert + price_delivery

print(total_delivery)
