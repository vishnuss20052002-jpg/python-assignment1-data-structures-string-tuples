#list creation
age_list = [24, 25, 26, 27, 28]
print(age_list)
[24, 25, 26, 27, 28]
name_list = ["Arun", "Vishnu", "Anu", "Rahul", "Meera"]
print(name_list)
['Arun', 'Vishnu', 'Anu', 'Rahul', 'Meera']
#List Operations / Modifications:
name_list.append("Yazhini")
print(name_list)
['Arun', 'Vishnu', 'Anu', 'Rahul', 'Meera', 'Yazhini']
age_list.insert(2, 30)
print(age_list)
[24, 25, 30, 26, 27, 28]
name_list.remove("Yazhini")
print(name_list)
['Arun', 'Vishnu', 'Anu', 'Rahul', 'Meera']
age_list.pop()
28
age_list.extend([29, 30, 26])
print(age_list)
[24, 25, 30, 26, 27, 29, 30, 26]
age_list.sort(reverse=True)
print(age_list)
[30, 30, 29, 27, 26, 26, 25, 24]
print("Maximum age:", max(age_list))
print("minimum age:",min(age_list))
print("sum of ages:",sum(age_list))
#Accessing List Elements:
print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])
#DICTIONARY (Creation, Modification and Access)
student_marks = { "Arun": 85, "Vishnu": 90,"Anu": 78,"Rahul": 88,"Meera": 95}
print(student_marks)
print("Vishnu' Mark:", student_marks["Vishnu"])
student_marks["Janani"] = 80
print(student_marks)
student_marks["Anu"] = 82
print(student_marks)
print("Keys:", student_marks.keys())
print("values",student_marks.values())
print("items:",student_marks.items())
#SETS (Operations)
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print(my_set)
my_set[4]='s'
set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}

print(set1)
print(set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
#Operators & Conditional Statements (IF, ELIF, ELSE)
score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid Score! Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep it up.")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")
