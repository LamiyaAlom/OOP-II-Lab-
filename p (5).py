P = int(input("value for P: "))
Q = int(input("value for Q: "))

temp_1 = P
P = Q
Q = temp_1

print("Value of P after swapping: ", P)
print("Value of Q after swapping: ", Q)