unit = input("Enter temprature in ceilsus or farhneit (C/F) : ")
temp = float(input("Enter the temprature : "))
if unit == "C":
    temp = round((temp * 9)/5 +32, 1)
    print(f"temprature in farhnite is : {temp}")
elif unit == "F":
    temp = round((temp-32)*5/9, 1)
    print(f"temprature in celcius is : {temp}")
else:
    print(f"{unit} is invalid unit of measurement.")
