#COMPULSORY TASK 2

#requesting user to enter 3 random product names

pr1 = input("Enter name of the first product here: ")
pr2 = input("Enter name of the second product here: ")
pr3 = input("Enter name of the third product here: ")

#requesting prices of said products

price1 = round(float(input("Enter price of the first product here: ")))
price2 = round(float(input("Enter price of the second product here: ")))
price3 = round(float(input("Enter price of the third product here: ")))

#calculating the total of all products

total= price1 + price2 + price3
print(round(total, 2))

#calculating the average price of the three products

aver = total/3
print(round(aver, 2))

#printing out the all the product information

print("The Total of", pr1, ",", pr2,",", pr3, "is R",total, "and the average price of the iterms are R", round(aver,2))
