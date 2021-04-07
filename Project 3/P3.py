import datetime
import time

print ("This will tell you the phase of the moon on the day you were born!")
myName = input("What is your name? ----> ")
print('Hello, ' + myName + '! ')

by = int(input("Please enter the year that you were born: "))
print('Please enter the month..')
bm = int(input("Ex: August = 08  ----> "))
bd = int(input("Please enter the day: "))

this_year = datetime.date.today().year
this_month = datetime.date.today().month
this_day = datetime.date.today().day

#Moon Formulas
MoonA = by / 100
MoonB = MoonA / 4
MoonC = (2 - MoonA) + MoonB
MoonE = 365.25 * (by + 4716)
MoonF = 30.6001 * (bm + 1)
JD = MoonB + MoonC + MoonE + MoonF
DaysSN = JD - 2451549.5
Cycles = DaysSN / 29.53
DaysIN = (Cycles - int(Cycles)) * 29.53



# If statements to display results
if 3 >= ((Cycles - int(Cycles)) * 29.53) :
    print("You were born during a New Moon! This phase occurs when the moon is in conjunction with the sun so that its dark side is toward the earth. Also, the thin crescent moon can be seen shortly after sunset for a few days after the actual occurrence of the new moon phase.")
if 3 < ((Cycles - int(Cycles)) * 29.53) <= 7:
    print("You were born during a Waning Crescent phase! Waning means that it's shrinkinng and getting smaller, while crescent refers to the curved sickle shape.")
if 7 < ((Cycles - int(Cycles)) * 29.53) <= 11:
    print("You were born during a Third Quarter phase! Third or last quarter moon means we see a quarter of the moon's day side, and the moon is three-quarters of the way through the cycle, as measured from one new moon to the next.")
if 11 < ((Cycles - int(Cycles)) * 29.53) <= 15:
    print("You were born during a Waning Gibbous phase! The waning gibbous phase is between a half moon and full moon. Waning means it is getting smaller.")
if 15 < ((Cycles - int(Cycles)) * 29.53) <= 18:
    print("You were born during a Full Moon phase! Spooky!")
if 18 < ((Cycles - int(Cycles)) * 29.53) <= 22:
    print("You were born during a Waxing Gibbous phase! Waxing gibbous means it's getting visually wider and wider from day to day, culminating in a full moon.")
if 22 < ((Cycles - int(Cycles)) * 29.53) <= 26:
    print("You were born during a First Quarter phase! It's the moon phase halfway between new moon and full moon.")
if 26 < ((Cycles - int(Cycles)) * 29.53) <= 30:
    print("You were born during a Waxing Crescent phase! The waxing crescent phase is the moon's first step toward fullness. And it's a very visible shift.")