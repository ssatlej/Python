def commonletters():
    str1 = input("Enter 1st string :")
    str2 = input("Enter 2nd string :")

    s1=set(str1)
    s2=set(str2)

    result = s1 & s2
    print(result)

commonletters()