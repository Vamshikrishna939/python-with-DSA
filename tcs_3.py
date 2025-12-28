def program(n):
    count = 0
    for i in range(0,n*10+1):
        if i % 10 == 0:
            x=i
            count +=x
    return count
print(program(10))        