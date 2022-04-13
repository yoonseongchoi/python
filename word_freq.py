#!/usr/bin/python3

import sys
import re
import string

f = open(sys.argv[1],'r')
string = f.readlines()
cys =""
for line in string:
	line = line.strip()
	line = re.sub('[-=,#/n\?!:^.@*|"]','',line)
	cys += line
f.close()
text = cys.split()
dic = {}
for w in text:
	if not w in dic:
		dic[w] = 1
	else:
		dic[w] +=1
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
most = int(sys.argv[2])
for i in range(0,most):
	print(result[i])
