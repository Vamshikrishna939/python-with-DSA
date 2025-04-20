a=str(input("enter the box number"))
if a[0] in "aceg":
    if a[1] in "1357":
       print("black")
    else:
        print("white")
else:
    if a[1] in "1357":
       print("white")
    else:
        print("black")           
