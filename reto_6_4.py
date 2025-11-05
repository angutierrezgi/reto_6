print("----Biggest Sum of Consecutive Numbers----")

while True:
    try:
        count: int = int(input("How many numbers do you want to enter?: "))
        break
    except (TypeError, ValueError):
        print("Not valid input. Must be an integer!")
        continue

num_1: int = 0
biggest_sum: int = 0

for number in range(count):
    while True:
        try:
            num_2: int = int(input(f"{number + 1}°. "))
            sum: int = num_1 + num_2
            if sum > biggest_sum:
                aux_1: int = num_1
                aux_2: int = num_2
                biggest_sum = sum
            num_1 = num_2
            break
        except (TypeError, ValueError):
            print("Value must be an integer!")
            continue
            
print(f"The sum of {aux_1} and {aux_2} was the biggest, resulting in {biggest_sum}")