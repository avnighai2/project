num = int(input("enter the number:"))
t = num
numlen = 0 

while t>0:
    numlen = numlen+1
    t = int(t/10)

if numlen > 4:
    numlen = int(numlen/2)
    a = 0 
    while num > 0:
        rem = num % 10 
        if a == numlen:
            midone = rem 
        elif a == (numlen - 1):
            midtwo = rem 
            num = int(num/10 )
            a = a + 1
    product = midone * midtwo 
    print("\n product of mid digits (" +str(midone)+ "*" +str(midtwo)+") = ", prod)

else:
    print("\n it's not a 4 for or more than a 4 digit number")