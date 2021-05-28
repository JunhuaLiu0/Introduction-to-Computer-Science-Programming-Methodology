while True:
    num = input('Input an integer: ')
    if num.isdigit() and int(num) > 0:
        print("m\tm+1\tm**(m+1)")
        n = int(num)
        for i in range(1,n+1):
            print(i,"\t",i+1,"\t",i**(i+1),"\t")
        break
    else:
        print('Please input an positive integer')