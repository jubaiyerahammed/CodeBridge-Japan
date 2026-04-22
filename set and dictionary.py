student_roll_name_dict={
    1:'abul',
    2:'babul',
    3:'cabul',
    4:'dabul',
    5:'eabul'
}
student_roll_name_dict[6]='Fabul'
#student_roll_name_dict.pop(2)
#print(student_roll_name_dict)

#for key, value in student_roll_name_dict.items():
 #   print('Roll Number:', key, ', Name:', value)


#print(student_roll_name_dict.keys())
#print(student_roll_name_dict.values())



student_roll_marks_dict={
    1:100,
    2:99,
    3:85,
    4:80,
    5:75
}


number_list=student_roll_marks_dict.values()

#total_marks=0
#for marks in number_list:
  #  total_marks=total_marks+marks
total_marks=sum(number_list)
average_marks=total_marks/len(student_roll_marks_dict) if len(student_roll_marks_dict)>0 else 0

print('average marks:', round(average_marks,2))  

Student_info_list=[]
while True:
    roll_number=input('Enter the roll number:')
    if roll_number=='exit':
        break
    roll_number=int(roll_number)
    student_age=input('Enter the student age:')
    student_age=int(student_age)

    student_name=input('Enter the student name:')

    student_info={
        'roll_number':roll_number,
        'student_age':student_age,
        'student_name':student_name

    }
    Student_info_list.append(student_info)
#print('Student Information:', Student_info_list)

for student in Student_info_list:
    print('Roll Number:',student['roll_number'], 'Age:', student['student_age'], 'Name:',student['student_name'])