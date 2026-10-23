#TIP CALCULATOR PROJECT
print("welcome to the tip calculator")
Bill=float(input("what was the total bill? in dolor"))
Tip=int(input("how much percent tip would you like to give ? 5,10,15"))
Split=int(input("how many people to split the bill ?"))
Total_Bill=((Bill/Split)*(Tip/100)+(Bill/Split))
print("each person should pay " + " " +f"{Total_Bill}")

