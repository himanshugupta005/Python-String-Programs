s=input("input the string")
d={}
l=s.split(" ")
for item in l:
     c=0
     for i in range(len(l)):
          if(item==l[i]):
               c+=1
               d.update({item:c})
               print(f"the frequency of each word is {d}")

