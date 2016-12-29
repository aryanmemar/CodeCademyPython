n = 21

    
def digit_sum(n):
    digit = []
    n = str(n)
    for i in n:
        i = int(i)
        digit.append(i)

    return sum(digit)

print digit_sum(n)