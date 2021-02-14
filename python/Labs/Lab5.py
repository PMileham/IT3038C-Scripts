
print("This will return the prime numbers in between two integers.")
BottomNum = int(input("What is the first number?"))
TopNum = int(input("What is the second number?"))
print ("Prime numbers between", (BottomNum), "and", (TopNum), "are:" )

for num in range(BottomNum, TopNum +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break

            else:
                print(num)

#already_printed = set()
#for item in g_data:
 #   header = item.find_all("div", {"class": InnprodInfos"})
  #  item = header[0].contents[0].text.strip()
   # if item not in already_printed:
    #    print(item)
     #   already_printed.add(item)