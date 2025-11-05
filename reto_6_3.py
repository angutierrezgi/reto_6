print("----Prime Number Checker----")

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for divisor in range(2, int(num**0.5) +1):
        if num % divisor == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        try:
            count: int = int(input("How many numbers do you want to check?: "))
            break
        except (TypeError, ValueError):
            print("Not valid input. Must be an integer!")
            continue
    prime_list = []
    for number in range(count):
        while True:
            try:
                num: int = int(input(f"{number + 1}°. "))
                if is_prime(num):
                    prime_list.append(num)
                break
            except (TypeError, ValueError):
                print("Input should be an integer!")
                continue

    print(f"The prime numbers you entered are: {prime_list}")