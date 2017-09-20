file = open("TheVictors.txt","r")
wordlist = []
worddic = {}
for line in file:
	line = line.replace(",","").replace("!","").replace(".","").strip().lower().split()
	for word in line: 
		if word in worddic: worddic[word] += 1
		else: worddic[word] = 1

wordvalue = sorted(list(worddic.items()),key = lambda x:x[1],reverse=True)
for value in range(15): print(wordvalue[value][0],wordvalue[value][1])