#search for number x in this tuple (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64
i = 0

while i < len(tpl):
    if tpl[i] == x:
        print("Number Found at index", i)
          
    i += 1  # Move to the next index
