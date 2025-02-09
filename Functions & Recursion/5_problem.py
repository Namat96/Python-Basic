#.......WAF to print element of list in a single line
cities = ["lahore", "Multan", "islambad", "Karachi"]

cities = ["lahore", "Multan", "islambad", "Karachi"]

def print_lst(lst):  # Changed 'list' to 'lst' to avoid conflict with the built-in 'list' function
    for item in lst:
        print(item, end=" ")  # Added a space after each item for better readability

print_lst(cities)  
        