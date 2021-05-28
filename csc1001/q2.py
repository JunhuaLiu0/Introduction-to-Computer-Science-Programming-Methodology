num = input("Enter an integer: ")
if int(num)<=0:
    print("Your number should be a postive number！")
else:
    num_list=list(num)
    for i in range(len(num_list)):
        print(num_list[i])
