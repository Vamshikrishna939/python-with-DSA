def generate_triangle(n):

    # Your code here
    triangle = []
    for i in range(1,n+1):
            triangle.append(i*"*")
    return triangle        
print(generate_triangle(5))