s1=input("enter first string")
s2=input("enter second string")
a=list(set(s1)&set(s2))
print("the common letters are:")
for i in a:
    print(i)