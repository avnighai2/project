# Program to check if a student's age is eligible for enrollment

def check_enrollment(age):
    if 10 <= age <= 20:
        return "Student is eligible to enroll."
    else:
        return "Student is not eligible to enroll."

# Get input from the user
try:
    student_age = int(input("Enter the student's age: "))
    result = check_enrollment(student_age)
    print(result)
except ValueError:
    print("Please enter a valid number for age.")
