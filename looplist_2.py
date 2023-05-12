num = [5, 2, 3, 1, 3]
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[4])

# for i in range(0, len(num)):
#     print(num[i])

for n in num:
     print(n)

# def addNumbers(num1, num2, num3):
#     return num1 + num2 + num3
# num1 = int(input("Enter num 1:"))
# num2 = int(input("Enter num 2:"))
# num3 = int(input("Enter num 3:"))

# print(addNumbers(num1, num2, num3))

def addNumbers(num):
    total = 0

    for n in num:
        total += n
        print(n, total)
    return total
print(addNumbers([3, 5, 6, 2]))

def fruitcost(apple, banna, strawbery, pineapple)
    total = 0
    