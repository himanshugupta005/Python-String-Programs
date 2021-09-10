string = input()
if len(string) <3:
    print(string)
   elif string[-3:] == 'ing':
      print(string + 'ing')
    else:
     print(string + 'ly')
