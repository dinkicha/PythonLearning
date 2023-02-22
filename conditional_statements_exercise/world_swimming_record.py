import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_swimming_one_meter = float(input())

needed_to_swim = distance_in_meters * time_in_seconds_for_swimming_one_meter
seconds = math.floor(distance_in_meters / 15) * 12.5

total_time = needed_to_swim + seconds

if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.')
