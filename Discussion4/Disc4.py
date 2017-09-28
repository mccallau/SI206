import re
file = open('mbox-short.txt','r')
for line in file:
	if re.search('^From .*', line):
		num = re.findall('[0-9]', line)
		name = re.findall('(\S*)@',line)
		print(line)
		for obj in num:
			print(obj, end = " ")
		print('\n')
		for obj in name:
			print(obj)
		print('\n')
