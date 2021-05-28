def sqrt(n):
    lastGuess = n/2
    nextGuess = (lastGuess + (n / lastGuess)) /2
    while abs(nextGuess - lastGuess) >= 0.001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) /2
    print(nextGuess)
n =float(input("please enter an positive integer: "))
sqrt(n)
