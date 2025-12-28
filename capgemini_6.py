def program():
    d = int(input("enter no of delars"))
    for i in range (d):
        c,b=map(int,input("enter the cars bikes").split())
    print(c*4+b*2)    
print(program())         