student1 = {'name' : "'Kirill", 'gpa': 4.0, 'LastName': 'Gorshenin'}
student2 = {'name': 'Hamza', 'gpa': 3.7, 'LastName': 'Smith'}

for info in student1:
    print('key is:', info)

for info in student1.keys():
    print('key is:', info)

print('Looping key')
for key in student1.keys():
    print('value is:', student1[info])

print('Looping value')
for value in student1.values():
    print('value is:', value)

print()
print('looping keys and values')
for key, value in student1.items():
    print('key is:', key)
    print('value is:', value)

print('********** Nesting dictionaries in list')
class_2020 = [student1, student2]
for student in class_2020:
    print('Name of the student:', student['name'])
    print('Gpa of the student:', student ['gpa'])
    print('LastName of the student:', student ['LastName'])
    print('--------------------')

print()
dclass_2020 = {'student1': student1, 'student2': student2}
for key, value in dclass_2020.items():
    print('Key of the element:', key)
    print('Value of the element:', value)
    print('Name of the student:', value['name'])
    print('Gpa of the student:', value['gpa'])
    print('LastName of the student:', value['LastName'])
    print('--------------------')
print()











