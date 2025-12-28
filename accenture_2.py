def program(m,n):
    count = 0
    flag = 0
    for i in range (1,n+1):
        if i%m == 0:
            count += i
        else:
            flag += i
    return abs(flag - count)    
m,n=map(int,input("enter m and n values ").split())
print(program(m,n))      

