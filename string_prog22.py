string="i am a python programmr"
word=""
words=[]

string=string+""

for i in range(0,len(string)):
    if(string[i]!=''):
        word=word+string[i]
    else:
            words.append(word)
            word=""

small=large=words=[0]

for k in range(0,len(words)):
    if (len(small)>len(words[k])):
        small=words[k]
    if(len(large)<len(words[k])):
        large=words[k]

        print("smallest word:" + small)
        print("largest:" + large)

