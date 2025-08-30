# question 1:

n = int(input("enter the number: "))
even = 0
pow = 1
m = 0
while n >= 1:
    m = n % 10
    if m % 2 == 0:
        even += m * pow
        pow *= 10
    n //= 10
print(even)

# # question 2:

n = int(input("enter the number of students: "))
count = 0
for i in range(n):
    grade = float(input("enter the grade of student: " ))
    if 10 <= grade <= 15:
        count += 1
print(count)

# # question 3:

n = int(input("enter the number of students: "))
sum = 0
count = 0
for i in range(n):
    grade = float(input("enter the grade of student: "))
    if grade >= 15 :
        sum += grade
        count += 1
print("the number of grades wich are more than 15: ", count)
average = sum / count
print("the average of grades wich are more than 15: ", average)

# # question 4:

n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end= " ")
    print()