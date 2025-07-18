student_sum=0
student_height= input("please input the height of students in cm\n" ).split()
for n in range(0, len(student_height)):
 student_height[n]=int(student_height[n])
 student_sum +=student_height[n]
average_height=round(student_sum/(n+1))
print(f"student_height are {student_height} \n and the average_hight is : {average_height}")