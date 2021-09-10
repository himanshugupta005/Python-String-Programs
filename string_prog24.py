def unique_list(l):
    temp=[]
    for x in l:
        if x not in temp:
            temp.append(x)
        return temp

text_str=["python" , "exercises" , "pratices" , "solution", "exercises"]
print("original string")
print(text_str)
print("\nafter removing duplicate words from the said list of strings:")
print(unique_list(text_str))