import re

#Regular expressions practice for text surfing

numberlist = []
file = open("mbox-short.txt","r")
for line in file:
	if re.search("^X-DSPAM-Confidence:",line):
		try:
			number = re.findall("^X-DSPAM-Confidence: ([^ ]*)",line)
			number = number[0].strip()
			numberlist.append(float(number))
		except:
			pass
print(max(numberlist))
print(min(numberlist))
print("{:.4f}".format(sum(numberlist)/len(numberlist)))