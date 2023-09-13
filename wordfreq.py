def wordfreq():
    str1=input("Enter The string : ")
    li = str1.split( )
    d={}
    for i in li:
        if i not in d.keys():
            d[i]= 0
        d[i]+=1
    print(d)

wordfreq()


