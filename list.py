li=[5,9,16,56,66]
c=1
for i in range(0,len(li),1): #here last column 1 refers to increment in the no 
        c = c * li[i]
print(c)
li.insert(2,99) #insert the no 99 at index 2
print(li)
li.sort() #sorts from ascending to descending
print(li)
d=li.index(9)  #find the index
print(d)
print(li[2:5])                        #silicing of the list
print(li[::-1])