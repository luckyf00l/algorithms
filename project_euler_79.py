# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 17:14:36 2013

@author: Michael
"""
import pandas as pd
import re
def valid(string):
    rege='[0-9]*'+string[0]+'[0-9]*'+string[1]+'[0-9]*'+string[2]
    return rege


def valid_sub(string,substring):
    return not(re.match(valid(substring),string)==None)


tries=pd.read_csv('keylog.txt',header=None)

code=73100000

while True:
    checkall=True
    for i in tries.values:
       
       checkall=checkall and valid_sub(str(code),str(i[0]))
       print code,i,checkall       
       if not checkall:
           code+=1
           break
    
    
    if checkall:
        break
    