class Student(object):
	def __init__(self, first, last, years_UM, dept="undeclared"):
		self.first_name = first
		self.last_name = last
		self.years_umich = years_UM
		self.department = dept

	def get_full_name(self):
		return "{} {}".format(self.first_name,self.last_name) # see the String Formatting chapter in the textbook to learn about this syntax for formatting strings if you are not yet familiar!

	def likely_credits(self):
		courses_credits  = {"SI 206":4, "SI 106":4, "SI 110":4, "ENG 290":3, "HIST 450":3, "HIST 124":4,"LING 210":4,"LING 340":3}
		likely = 0
		if "HIST" in self.department.upper():
			for k in courses_credits.keys():
				if "HIST" in k:
					likely += courses_credits[k]
		elif "SI" in self.department.upper():
			for k in courses_credits.keys():
				if "SI" in k:
					likely += courses_credits[k]
		elif "LING" in self.department.upper():
			for k in courses_credits.keys():
				if "LING" in k:
					likely += courses_credits[k]
		else:
			likely = sum(courses_credits.values())
		return likely

	def __str__(self):
		if self.department == "undecided":
			return "{} is still deciding their department!".format(self.get_full_name())
		else:
			return "{} is in the {} department right now.".format(self.get_full_name(),self.department)

	def shout(self, phrase_to_shout):
		print(phrase_to_shout)


###### SAMPLE INSTANCE CREATION
one_student = Student("Jackie","Cohen",10,"SI")
student2 = Student("Ayo","Akonikun",3,"SI")
student3 = Student("Dorothy Jane", "Vaughan",5,"EECS and MATH")
student4 = Student("Agnes","Liu",1,"History")


##### WRITE YOUR UNIT TESTING HERE TO CHECK YOUR OUTPUT ANSWERS FOR THE QUESTIONNAIRE.
# What is the output of the code print(one_student) in the program?
# What is the output of the code print(student2) in the program?
# What is the output of the code print(student4.likely_credits()) in the program?
# What is the output of the code print(student3.likely_credits()) in the program?
