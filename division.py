n=int(input("enter the number"))
print("the numbers divisible by ",n ,"are")
for i in range (1,100):
    if i%n==0:
        print(i)