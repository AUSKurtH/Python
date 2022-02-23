# Author: Kurt
# Date: 2022/02/16
# Task: 25, create an elif table

Mark = int(input("Please enter the student's final mark: "))

if(Mark >= 0 and Mark <50):
    print("Fail")
elif(Mark >=50 and Mark <60):
    print("Pass")
elif(Mark >=60 and Mark <75):
    print("Credit")
elif(Mark >=75 and Mark <85):
    print("Distinction")
elif(Mark >=85 and Mark <100):
    print("High Distinction")
else:
    print("Please enter a student grade from 0-100")