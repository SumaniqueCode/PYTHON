# Created on 2024/03/05
# By Suman Regmi

import re
string = "This is test string for the python program. This has multiple words"
data = re.split(" ", string)
result = {}
for n in data:
    keys = result.keys()
    if n in keys:
        result[n] +=1
    else:
        result[n]=1
print("The frequency of all words of string is: ", result)