

def program(m,n):
    if n<=m:
     count = 0
     for i in range(n,m+1):
        x=i**3
        count+=x
    return count
print(program(4,2))

