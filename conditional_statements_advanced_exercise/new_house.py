import math
plants = input()
count_plants = int(input())
budget = int(input())

roses = 5
dahlia = 3.80
tulip = 2.80
narcissus = 3
gladiolus = 2.50
price = 0

if plants == 'Roses':
        price = count_plants * roses
        if count_plants > 80:
            price = price * 0.90
elif plants == 'Dahlias':
        price = count_plants * dahlia
        if count_plants > 90:
            price = price * 0.85
elif plants == 'Tulips':
        price = count_plants * tulip
        if count_plants > 80:
            price = price * 0.85
elif plants == 'Narcissus':
        price = count_plants * narcissus
        if count_plants < 120:
            price = price * 1.15
elif plants == 'Gladiolus':
        price = count_plants * gladiolus
        if count_plants < 80:
            price = price * 1.20

diff = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {count_plants} {plants} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')




