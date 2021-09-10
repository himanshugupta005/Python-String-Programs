import re
ip="213.08.089.245"
string=re.sub('\.[0]*', '.', ip)
print(string)