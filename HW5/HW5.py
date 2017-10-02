import re
file = open("regex_sum_31742.txt",'r')
allnum = []
for line in file:
	if len(re.findall('[0-9]',line))>0:
		num = re.findall('[0-9]+',line)
		for n in num:
			allnum.append(int(n))
print(sum(allnum))
