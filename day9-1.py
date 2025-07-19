Student_scores={
    "Harry":81 ,
    "Ron":78 ,
    "hermione":99,
    "Draco":74 ,
    "Neville":62,

}

Student_grade = {}
for student in Student_scores:
    scores=Student_scores[student]
    if scores>90:
        Student_grade[student]="Outstanding"
    elif scores>80  :
        Student_grade[student]="Exceeds expectation"
    elif scores>70  :
        Student_grade[student]="Acceptable"
    else :
        Student_grade[student]="Fail"
print(Student_grade) 