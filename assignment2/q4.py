def isAnagram(s1,s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("is an anagram")
    else:
        print("is not an anagram")
s1 = input("please input the first word: ")
s2 = input("please input the second word: ")
isAnagram(s1,s2)
