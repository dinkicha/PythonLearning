year_tax = int(input())
price_shoes = year_tax - 0.40 * year_tax
price_clothes = price_shoes - 0.20 * price_shoes
price_basketball_ball = price_clothes / 4
price_basketball_accessories = price_basketball_ball / 5
total_price = year_tax + price_shoes + price_basketball_ball + price_clothes + price_basketball_accessories

print(total_price)
