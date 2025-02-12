#..... write recursive function to print the sum of first n natural number
def calcult_sum(n):
    if (n == 0):
        return 0
    return calcult_sum(n-1) + n   
sum = calcult_sum(5)   
print(sum)