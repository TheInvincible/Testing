student = {"name" : 'joan', "age" : 20}

print (student)

student["year"] = "second"

print (student)

for key, value in student.items():
	print (key, value)

del student["year"]

print (student)

