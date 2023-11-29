color_one=input("Enter the color1:-")
color_second=input("Enter the color2:-")

if color_one=="red" or color_one=="blue" or color_one=="yellow":
    print("")
else:
    print("Error: Invalid Colour_one")

if color_second=="red" or color_second=="blue" or color_second=="yellow":
    print("")
else:
    print("Error: Invalid Colour_second")
    
if color_one==color_second:
    print("Error: The two colours you entered are the same.") 
      
if (color_one=="red" and color_second=="blue"):
    print("purple")

if (color_one=="red" and color_second=="yellow"):
    print("orange")
    

if (color_one=="blue" and color_second=="red"):
    print("purple")  
    
if (color_one=="blue" and color_second=="yellow"):
    print("green")  

if (color_one=="yellow" and color_second=="red"):
    print("orange") 

if (color_one=="yellow" and color_second=="blue"):
    print("green") 
    
                  
  


    
