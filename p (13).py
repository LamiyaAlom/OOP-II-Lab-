def check_prime():
    num = int(input("Enter a number: "))

    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                print(f"{num} is not a prime number.")
                print(f"It is divisible by {i}.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
check_prime()
