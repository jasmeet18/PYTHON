@@ -0,0 +1,167 @@
i = 1
while i <= 10:
    print(i)
    i += 1


print("Number Pattern ")
row = 5
for i in range(1, row + 1, 1):
     for j in range(1, i + 1):
        print(j, end=' ')
     print("")


s = 0
n = int(input("Enter number "))
for i in range(1, n + 1, 1):
     s += i
print("\n")
print("Sum is: ", s)


n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)


numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)


num = 75869
count = 0
while num != 0:
      num = num // 10
      count = count + 1
print("Total digits are:", count)


n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()


list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)


for num in range(-10, 0, 1):
    print(num)


for i in range(5):
    print(i)
else:
    print("Done!")


start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


num1, num2 = 0, 1

print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res


num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
         factorial = factorial * i
    print("The factorial of", num, "is", factorial)


num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")


input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))


n = 5
start = 2
sum_seq = 0
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

