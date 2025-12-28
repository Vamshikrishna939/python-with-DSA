def program():
    d=int(input("enter the no dealers"))
    vechile = []
    for i in range (d):
        c,b = map(int,input("enter the cars bikes").split())
        vechile.append((c,b)) ##tuple
    for i in range (d):
        print(f"dealars {i+1} , {vechile[i][0]} cars ,{vechile[i][1]} bikes")       
    return "all data loaded sucessfully"    
print(program())