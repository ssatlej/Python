def liststodict():
    li1=[]
    li2=[]
    li1 = input("Enter 1st List : ").split()
    li2 = input("Enter 2nd list : ").split()
    d=dict(zip(li1,li2))
    print(d)
liststodict()