print("welcome to our website")
a=input("what is your name ?\n")
print("hello ?",a)
b=str(input("what do you want?"))
if(b=="shirt"):
    print("it is available")
    c=int(input("what is the size "))
    if(c==30 ):
      print("it is available")
      d=str(input("which color do you want"))
      if(d=="pink"):
        print(b,"it is available",d)
      else:
        print(b,"it is not available",d)
    else:
      print(b,"it is not available")
elif(b=="pant"):
    print("it is available")
    c=int(input("what is the size "))
    if(c==30 or c==48 ):
      print("it is available")
      d=str(input("which color do you want"))
      if(d=="green"):
        print(b,"it is available")
      else:
        print(b,"it is not available")
elif(b=="hoodie"):
    print("it is available")
    c=int(input("what is the size "))
    if(c==30 or c==32 ):
      print("it is available")
      d=str(input("which color do you want"))
      if(d=="green" or "white" or "black"):
        print(b,"it is available in color",d)
      else:
        print(b,"it is not available",d)
    else:
      print(b,"it is not available")
else:
  print(b,"it is not available")