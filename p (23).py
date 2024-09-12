import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
num1 = int(input("first number: "))
num2 = int(input("second number: "))
print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")
