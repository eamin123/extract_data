import re
import os
import pandas as pd
#read RSI file
f = open('/Users/eamin/Downloads/data_cmd.log')
fo = open('/Users/eamin/Downloads/from_data_cmd.log','w')
myflag = False
myflag2 = True
i = 1
for lines in f:
    #lines = f.readlines()
    matchObj = re.search(r'q-[0-9][0-9]', lines)
    matchObj2 = re.search (r'^$', lines)
    #print(lines)
    #print(matchObj)
    if(matchObj):
        print(lines)
        fo.write(lines)
        myflag = True
    elif(myflag):
        #print(lines)
        fo.write(lines)
        print(' ######## Set is complete #####')
        i = i + 1 
        print(i)
        myflag = False
        myflag2 = True
    elif(matchObj2 and myflag2 ):
        continue 
    else:
        continue 

print('data extraction is complete')
print(i)
