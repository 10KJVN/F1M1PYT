myList = [3, 4, 6, 1, 8]

lowest_number = 1000000000
for eachNumber in myList:
    print(eachNumber)
    if eachNumber < lowest_number:
        lowest_number = eachNumber
print("lowest number: ", lowest_number)