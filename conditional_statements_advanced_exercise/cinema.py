projections = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns
if projections == 'Premiere':
    income = capacity * 12
elif projections == 'Normal':
    income = capacity * 7.50
elif projections == 'Discount':
    income = capacity * 5.00

print(f'{income:.2f} leva')