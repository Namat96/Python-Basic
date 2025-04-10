weight = float(input("Enter the wight : "))
unit = input("enter the unit kilogram or ponds (K or L) : ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} is not valid") 
print(f"your wight is : {weight} {unit}")       