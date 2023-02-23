product = input()
city = input()
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.50
        print(price * quantity)
    elif product == 'water':
        price = 0.80
        print(price * quantity)
    elif product == 'beer':
        price = 1.20
        print(price * quantity)
    elif product == 'sweets':
        price = 1.45
        print(price * quantity)
    elif product == 'peanuts':
        price = 1.60
        print(price * quantity)
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
        print(price * quantity)
    elif product == 'water':
        price = 0.70
        print(price * quantity)
    elif product == 'beer':
        price = 1.15
        print(price * quantity)
    elif product == 'sweets':
        price = 1.30
        print(price * quantity)
    elif product == 'peanuts':
        price = 1.50
        print(price * quantity)
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
        print(price * quantity)
    elif product == 'water':
        price = 0.70
        print(price * quantity)
    elif product == 'beer':
        price = 1.10
        print(price * quantity)
    elif product == 'sweets':
        price = 1.35
        print(price * quantity)
    elif product == 'peanuts':
        price = 1.55
        print(price * quantity)

