#Converting Square feet to Acres
SquareFeet = float(input('How many square feet do you want to convert into Acres?'))
while (SquareFeet <= 0):
    SquareFeet = float(input('How many square feet do you want to convert to Acres (positive values only)'))
    #input of positive values will be accepted. 
Acres = float(SquareFeet/43560) #Process will happen here
if (Acres >=1): 
    print("That is equal to one or more Acres")
else: 
    print("That is less than an acre.")
    #above line is shown. 