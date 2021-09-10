s=input()
s1="abcdefghijklmnopqrtuvwxyz"
c=0
for i in s1:
    if i in s:
        c=c+1
    if c==26:
        print("panagram")
    else:
        print("not panagram")