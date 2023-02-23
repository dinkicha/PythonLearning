degress = int(input())
time = input()
outfit = None
shoes = None

if time == 'Morning':
    if 10 <= degress <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degress <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degress >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time == 'Afternoon':
    if 10 <= degress <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degress <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degress >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time == 'Evening':
    if 10 <= degress <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degress <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degress >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degress} degrees, get your {outfit} and {shoes}.")