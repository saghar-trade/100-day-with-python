student_max=0
student_score=input("please enter the score of students\n").split()
for n in range(0, len(student_score)):
    student_score[n]=int(student_score[n])
    if student_score[n]>student_max:
        student_max=student_score[n]
print(f"student_max is :  {student_max}")  