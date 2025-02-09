#.......WAF to find factorial of number

def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact  # Return the final factorial

# Example usage
result = cal_fact(4)
print("Factorial:", result)  
