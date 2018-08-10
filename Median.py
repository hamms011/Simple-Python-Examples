print("Ungroup Median Calculation \n")

number_array = list()
number = int(input("Enter number of elements you want: \n"))

print("Enter your data")
for i in range(int(number)):
    n = input("Number: ")
    number_array.append(int(n))

print("Your entered data is:")
print(number_array)

sorted_list = sorted(number_array)
print("Arranged data is:")
print(sorted_list)
print("\n")

length = len(number_array)
center = length // 2


if length == 1:
    print("The median is: ", number_array[0])
elif length % 2 == 0:
    med = sum(sorted_list[center - 1:  center + 1]) / 2.0
    print("The median is: ", med)
else:
    print("The median is: ")
    print(sorted_list[center])