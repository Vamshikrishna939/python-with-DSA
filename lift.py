def calculate_lift_rounds(n, capacity):
    full_rounds = n // capacity
    
    # If there are any remaining people, add one more round
    if n % capacity != 0:
        return full_rounds + 1
    else:
        return full_rounds
    return full_roounds
print(calculate_lift_rounds(10,3))    