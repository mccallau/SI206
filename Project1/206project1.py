import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	opfile = open(file,"r")
	x=True
	datalist = []
	for line in opfile:
		if x==True:
			datakeys = line.strip().split(",")
			x=False
		else:
			values=line.strip().split(",")
			datadic = {}
			for pos in range(5):
				datadic[datakeys[pos]] = values[pos]
			datalist.append(datadic)
	return datalist
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorteddata = sorted(data,key = lambda x:x[col])
	topname = sorteddata[0]["First"]+" "+sorteddata[0]["Last"]
	return topname

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	classsizedic = {"Senior":0,"Junior":0,"Freshman":0,"Sophomore":0}
	for dic in data:
		classsizedic[dic["Class"]]+=1
	classsizelist =  list(classsizedic.items())
	classsizelist = sorted(classsizelist,key = lambda x:x[1], reverse=True)
	return classsizelist


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	DOBdic = {}
	for dic in a:
		DOB = dic["DOB"].split("/")
		day = DOB[1]
		if day not in DOBdic: DOBdic[day]=1
		else: DOBdic[day]+=1
	DOBlist = list(DOBdic.items())
	DOBlist=sorted(DOBlist,key=lambda x:x[1],reverse = True)
	return int(DOBlist[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer.  You will need to work with the DOB to find their current age.

	#Your code here:
	import datetime
	now = str(datetime.datetime.now())
	date = now.split()[0]
	datelist = date.split("-")
	AGElist = []
	for dic in a:
		DOB = dic["DOB"].split("/")
		Age = int(datelist[0])-int(DOB[2])
		if int(datelist[1])>int(DOB[1]):
			Age-=1
		AGElist.append(Age)
	return int(round(sum(AGElist)/len(AGElist),0))


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.

def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	sorteddata = sorted(a,key = lambda x:x[col])
	file = open(fileName,"w", newline="\n")
	for person in sorteddata:
		file.write(person["First"]+","+person["Last"]+","+person["Email"]+",")
		file.write("\n")
	file.close()




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

