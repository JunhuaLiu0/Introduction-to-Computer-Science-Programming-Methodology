while True:
    num = input('Input an integer: ')
    if num.isdigit() and int(num) > 2:
        l=[2]
        for i in range(2,int(num)+1):
            flag=True
            for j in l:
                if i%j==0:
                    flag=False
                    break
            if flag:
                l.append(i)
        print("The prime numbers smaller than %s include:" %num)
        n = 8
        for serial in range(len(l)):
            print(l[serial], end=" ")
            if (serial+1)%8 == 0:
                print("")
        break
    else:
        print('Please input an positive integer that is larger than 2')

