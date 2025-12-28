
def program(m, n):
    if n > m:
        m, n = n, m  # Ensure n is the smaller number

    count = 0
    for num in range(n, m + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                    count += num  # Add the prime number
    return count

# Example usage
print(program(10, 2))  # Output: 10 (2 + 3 + 5)
