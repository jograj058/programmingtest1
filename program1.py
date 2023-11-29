days=int(input("Enter numbers of days:-"))

if (days>31):
    print("Error: Invalid days Input")
    
months=int(input("Enter numbers of months:-"))
if (months>12):
    print("Error: Invalid Months Input")

Years=int(input("Enter numbers of years:-"))
if (Years>99):
    print(" “Error: Invalid years Input”")

if months==2:
   if days>29: 
       print("Error not valid days in feburary months")
       

print (days,"/" ,months,"/",Years)       
            

        