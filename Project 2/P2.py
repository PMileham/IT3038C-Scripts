import datetime
import time

print ("This will calculate exactly how old you are and display when your golden birthday is!")
print("A golden birthday is when you turn the age of the day your birthday is on. So if your birthday is on the 13th, your golden birthday would be when you turn 13 on the 13th.")
myName = input("What is your name? ----> ")
print('Hello, ' + myName + '! ')

by = int(input("Please enter the year that you were born: "))
bm = int(input("Please enter the month: "))
bd = int(input("Please enter the day: "))

this_year = datetime.date.today().year
this_month = datetime.date.today().month
this_day = datetime.date.today().day

age_yearRN = this_year - by - 1
age_monthRN = abs(this_month-bm - 2)
age_dayRN = abs(this_day-bd)

print ("Your age is: ", age_yearRN, "Years, ", age_monthRN, "Months, ", age_dayRN, "Days, ")
print ("Your golden birthday will be when you are", bd, "years old.")
print("Which is in.........")
time.sleep(2.5)
print("about", bd - age_yearRN, "years!" )
if bd - age_yearRN < 0:
    print("Oh no! You already had your golden birthday!")
elif bd - age_yearRN == 0:
    print("You had/have your golden birthday this year!!")