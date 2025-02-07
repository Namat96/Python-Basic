# name = input("Enter name : ")
# print("Hello", name, "! welcome to cryptography")
# radius = 5
# area = 3.14*radius*radius
# print("Area : ", area)
# a = int(input(" Enter NO : "))
# b = int(input(" Enter NO : "))
# print("Sum = ", a+b)
# num = int(input(" Enter NO : "))
# if num % 2 == 0:
#      print(num, "is an even number")
# else:
#      print(num, "is an even number")
# a = int(input(" Enter NO : "))
# b = int(input(" Enter NO : "))
# c = int(input(" Enter NO : "))
# if a>=b and a>=c:
#     largest = a
# elif b>=a and b>=c:
#     largest = b
# else:
#     largest = c
# print("The largest number is:", largest)
# list = [1, 2, 3, 4]
# a = ["Apple", "3.14", 4, 6.2]
# for fruit in a:
#     print(after list in python
#     ) 
# a = ["Apple", "Banana", "Charry"]
# b = (1, 2, 3)
# c = (4, 5, 6)
# r = b + c
# print(r*3)
# print("Apple"in my a)
students_marks = {
    "Ali": 87,
    "Asif": 90,
    "Akram": 79,
    "Bilal": 94 
    
}
print('Student above 80 : ')
for student, marks in students_marks.items():
    if marks > 80:
                print(f"{student}: {marks}")
