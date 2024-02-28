#first
n = int(input("enter: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n or i == j:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()
#second
n = int(input("enter: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()
#third
n = int(input("enter: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end= " ")
    print()
#fourth
for i in range(100, 550, 50):
    for j in range(i, i+600, 100):
        print(j, end= " ")
    print()
#fiveth
for i in range(2, 16, 4):
    for j in range(i, i+12, 2):
        print(j, end= " ")
    print()