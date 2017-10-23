def FirstFactorial(num):

    i = 1
    while num >= 1:
        i = i * num
        num = num -1
    num = i
    return num
print FirstFactorial(raw_input())
