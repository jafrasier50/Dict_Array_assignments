print("============================")
print("======Factorial Wizard======")
print("============================")

number = int(input("Please Input Integer: "))

the_index = 0

product = 0

numbers_array = []
for the_index in range(1, number + 1):
    numbers_array.append(the_index)
i = number
while i > 0:
    if i == number:
        product = number * (i - 1)
    else:
        if i > 1:
            product = product * (i - 1)
    i -= 1
print(product, "product")
