def generate_rectangle(n, m):
    # Your code here
    rectangle = []
    for i in range(n):
         rectangle.append("*"*m)
    return rectangle     
    
print(generate_rectangle(3,2))     
         