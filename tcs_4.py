def program(n):
    if n==1:
       return 1
    elif n==2:
       return 2 + 1
    branches = [1,2]
    for i in range(2,n):
       next_b = branches[i-1]*branches[i-2]*2
       branches.append(next_b)
    return branches
print(program(5))   