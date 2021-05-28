def isValid(number):
    sum = sumOfEvenDoubleSpace(number) + sumOfOddPlace(number)
    if str(number)[0] == 4 and cardLength <=16 and cardLength >= 13:
        if sum % 10 == 0:
            print("The number is valid")
        else:
            print("The number is not valid")
    else:
        print("The number is not valid")
def sumOfEvenDoubleSpace(number):
    sum = 0
    stringNumber = str(number)
    if cardLength % 2 == 0:
        for i in range(0,cardLength,2):
            doubleNumber = (int(stringNumber[i]))*2
            sum += getDigit(doubleNumber)
    if cardLength % 2 != 0:
        for i in range(1,cardLength,2):
            doubleNumber = (int(stringNumber[i]))*2
            sum += getDigit(doubleNumber)
    return sum
def getDigit(number):
    stringNumber = str(number)
    if number > 9:
        return int(stringNumber[0]) + int(stringNumber[1])
    else:
        return int(stringNumber)
def sumOfOddPlace(number):
    stringNumber = str(number)
    sum = 0
    if cardLength % 2 == 0:
        for i in range(1,cardLength,2):
            sum += int(stringNumber[i])
    if cardLength % 2 != 0:
        for i in range(0,cardLength,2):
            sum += int(stringNumber[i])
    return sum
    
number=int(input('please enter your credit card numbers:'))
cardLength = len(str(number))
isValid(number)   