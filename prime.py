input_number = int(input("Enter number: "))
is_prime = True

for num in range(input_number-1, 1, -1):
    if input_number % num == 0:
        is_prime = False
        break
if is_prime:
    print("OPTIMUS PRIME")
else:
    print("Decepticon...")
