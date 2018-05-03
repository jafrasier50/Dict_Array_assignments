print("============================")
print("======Factorial Wizard======")
print("============================")

number = int(input("Please Input Integer: "))
total = 0
# numbers_array = []
# i = 0
# while i <= number:
#     numbers_array.append(i)
#     i = i + 1
#
# for the_num in numbers_array:
#     index = numbers_array.index(the_num)
#     total = total + (the_num * numbers_array[index + 1])
the_index = 0

# while the_index <= number + 1:
#     total = total + (the_index * (the_index + 1))
#     the_index = the_index + 1
#
# print (total)
product = 0

numbers_array = []
for the_index in range(1, number + 1):
    numbers_array.append(the_index)
print (numbers_array)
i = number
while i > 0:
    print (i)
    if i == number:
        product = number * (i - 1)
        print(product)
    else:
        product = product * (i - 1)
        print(product)
    i -= 1
print(product)
