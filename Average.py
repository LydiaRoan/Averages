grades = []

print("please enter numerical grades, one by one, then enter the word '-1' when you're finished")

teacherInput = 0

while teacherInput != -1:
    teacherInput = float(input())
    grades.append(teacherInput)
    
del grades[len(grades)-1] 

average = sum(grades) / len(grades)
print("the average of these grades is " + str(average))
if(average > 89):
	print("you have an A")
elif(average > 79):
	print("you have a B")
elif(average > 69):
	print("you have a C")
elif(average > 59):
	print("you have a D")
elif(average > 49):
	print("you have an F")

GPA = average/25
print("the GPA is " +str(GPA))

