def isNonpalindromic(number):
    if number <= 11:
        return False
    reverse = str(number)[::-1]
    if int(reverse) != int(number):
        if isPrime(number) and isPrime(int(reverse)):
            return True
        else:
            return False
    else:
        return False

def isPrime(number):
    if number == 1: 
        return False
    i = 2
    n = 0
    for j in range(2, int(number / 2)+1):
        if number % j == 0:
            n += 1
    if n == 0:
        return True
    else:
        return False

def main():
    number_palindrome_primes = 100
    n = 0
    i = 1
    while n < number_palindrome_primes:
        if isNonpalindromic(i):
            print(i, end="   ")
            n += 1
            i += 1
            if n % 10 == 0:
                print()
        else:
            i += 1
            continue


main()
         