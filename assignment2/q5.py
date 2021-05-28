lockers = [0 for i in range(100)]
final_lockers=[]
for i in range(1,101):
    for j in range(100):
        if (j+1)%i == 0:
            if lockers[j] == 0:
                lockers[j] = 1
            else:lockers[j] = 0     
for i in range(100):
    if lockers[i] == 1:
        final_lockers.append(i+1)
print("The lockers: ", end="")
for i in final_lockers:
    print(i, end=" ")
print("are open.", end="")