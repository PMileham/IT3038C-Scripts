import datetime
now = datetime.datetime.now()
print("This will display the current date and time.")
Namer = input("What is your name?")
print("Okay," + Namer + ".. The current date and time is: ")
print (now.strftime("%m-%d-%Y %H:%M:%S"))