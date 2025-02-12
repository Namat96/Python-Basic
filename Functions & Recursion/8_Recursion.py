def show(n):
    if n == 0:  # Base case: when n reaches 0, stop recursion
        print(n)
        return n
    show(n - 1)  # Recursive call: call show with n-1

show(5)

def fact(n):
    if(n == 1 or n==0):
        return 1
    return fact( n -1) * n
print(fact(3))   























