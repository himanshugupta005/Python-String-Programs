string=input("enter any string")
upper,lower,numeric,special=0,0,0,0
for i in range(len(str)):
    if(str[i]>='A'and str[i]<='Z'):
        upper+=1
    elif(str[i]>='a'and str[i]<='z'):
        lower+=1
    elif(str[i]>='1' and str[i]<='9'):
        numeric+=1
    else:
        special+=1
print("upper case letters: ", upper)
print("\nlower case: ", lower)
print("\nnumbers: ", numeric)
print("\nspecial characters: ", special)
