x = int(input())
y = input()
if y == "+":
    z = int(input())
    print(x + z)
elif y == "-":
    z = int(input())
    print(x - z)
elif y == "*":
    z = int(input())
    print(x * z)
elif y=="**":
    z = int(input())
    print(x**z)
elif y=="√":
    print(x**0.5)
elif y == "/":
    z = int(input())
    if x and z != 0:
        print(x / z)
    else:
        print("MATH ERROR")
else:
    print("SYNTAX ERROR")
