length_centimeters = int(input())
width_centimeters = int(input())
height_centimeters = int(input())
percent = float(input())

meters = length_centimeters * width_centimeters * height_centimeters
in_letters = meters * 0.001
taken = 0.17
needed_letters = in_letters * (1 - taken)
print(needed_letters)
