#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 1. В классе профессора Грубла только что был экзамен.
    # Напишите программу, которая принимает в качестве входящих данных оценку каждого ученика и то, сдал ли он экзамен.
    # Затем программе необходимо напечатать две вещи:
        # a. Был ли профессор Грубл последовательным в проставлении отметки “Passed” для студентов.
        # b. Если профессор Грубл был последовательным, выведите диапазон, в котором находится порог для сдачи экзамена.
        
def Exam(numb_of_students = 6):
    """This is Exam"""
    
    list_of_students = []
    marks_of_students = []
    professors_note = []
    marks_of_students_with_f_note = []
    marks_of_students_with_p_note = []
    import time

    for i in range(1, numb_of_students + 1):
        student = input("Name for student %s: " % i)
        mark = int(input("Mark for this student: "))
        note = input("Professors note for this student ('f'- failed or 'p'- passed): ")
        list_of_students.append(student)
        marks_of_students.append(mark)
        professors_note.append(note)
        if note == "f":
            marks_of_students_with_f_note.append(mark)
        elif note == "p":
            marks_of_students_with_p_note.append(mark)
        time.sleep(1)
        
    final_list = list(zip(list_of_students, marks_of_students, professors_note))
    print("STUDENT", "MARK", "PROFESSORS NOTE", sep='\t\t')
    for element in final_list:
        print(*element, sep='\t\t')
    if min(marks_of_students_with_p_note) < max(marks_of_students_with_f_note):
        print("Professor Gruble was not consistent in marking 'p'- passed for students.")
    else:
        print("Professor Gruble was consistent in marking 'p'- passed for students.",
             "And the range for passing the exam is from "
              + str(max(marks_of_students_with_f_note) + 1) + " to "
              + str(min(marks_of_students_with_p_note)) + ".", sep='\n')


# In[13]:


Exam(int(input("Input the number of students: ")))


# In[14]:


Exam(int(input("Input the number of students: ")))

