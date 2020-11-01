def getDigit(x):
    returnDigit = 0
    while x > 0:
        x //= 10
        returnDigit += 1
    return returnDigit


print(getDigit(2**512))
print(2**512)
