print("Ungroup Mean Calculation")

number_array = list()
number = int(input("Enter number of elements you want: "))
print("Enter your mean data")

for i in range(int(number)):
    n = input("Number: ")
    number_array.append(int(n))

print("\nThe mean is: ", sum(number_array) / number)
