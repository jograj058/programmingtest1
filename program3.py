a=int(input("enter your salary in euro:"))
b=str(input("enter country name you want to move:"))

if (b=="canada"):
    a*1.49
    if(a>56000):
      print("you are rich in canada with this salary",a)
    elif(a<56000):
        print("you are poor in canada with this salary",a)
        

if (b=="USA"):
    a*1.10
    if(a>45000):
      print("you are rich in usa with this salary",a)
    elif(a<45000):
        print("you are poor in usa with this salary",a)        


if (b=="combodia"):
    a*4000
    if(a>7649856):
      print("you are rich in combodiawith this salary",a)
    elif(a<7649856):
        print("you are poor in combodia with this salary",a)        
        

if (b=="uk"):
    a*86
    if(a>45423):
      print("you are rich in uk with this salary",a)
    elif(a<45423):
        print("you are poor in uk with this salary",a)        