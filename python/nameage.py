import time

start_time = time.time()

print('What is your name')
myName = input()
print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())
programAge = int(time.time() -start_time)
print(str(myAge) +"? Thats funny, i'm only ")
print("I wish I was " + str(myAge * 2) + " years old")  

time.sleep(3)
print("I'm tired. I'm going to sleep now...")