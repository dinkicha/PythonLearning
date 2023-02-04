count_pen = int(input())
count_markers = int(input())
liters = int(input())
percent_discount = int(input())

price_pens = count_pen * 5.80
price_markers = count_markers * 7.20
price_liters = liters * 1.20
price_for_all_materials = price_pens + price_markers + price_liters
price_with_discount = price_for_all_materials - (price_for_all_materials * percent_discount / 100)

print(price_with_discount)