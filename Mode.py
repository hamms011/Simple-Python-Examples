from statistics import *

print("Ungrouped Mode \n")

number_array = list()
number = int(input("Enter the number of elements you want: \n"))

print("Enter your data")
for i in range(int(number)):
    n = input("Number: ")
    number_array.append(int(n))

try:
    print("The mode is: ", mode(number_array))
except StatisticsError:
    print("There is no mode in your data.")
