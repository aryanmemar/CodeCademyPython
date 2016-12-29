def factorial(x):
    total = 1
    for i in range(1,x+1):
        total = total * i
        
    return total

x = 4

print factorial(x)
    