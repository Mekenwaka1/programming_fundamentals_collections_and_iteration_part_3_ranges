one_to_one_hundred = range(1, 101)

for num in one_to_one_hundred:
    if num % 3 == 0 and num % 5 == 0:
        print("Bitmaker")
    elif num % 3 == 0:
        print("Bit")
    elif num % 5 == 0:
        print("Maker")
    else:
        print(num)
