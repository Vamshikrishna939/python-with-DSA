def generate_square(n):
   
    square = []
    for i in range(n):
        square.append("*"*n)
    return square
print(generate_square(5))  
