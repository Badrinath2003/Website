def gather_course_details():
    print("Welcome to the Course Joining Process")
name = input("Please enter your name: ")
designation = input("Please enter your designation: ")
course = input("Please enter the course you would like to join: ")
location = input("Please enter your preferred location: ")
fee_proof = input("Please share the fee payed proof: ")
print("\nCourse Joining Details:")
print(f"Name: {name}")
print(f"Designation: {designation}")
print(f"Course: {course}")
print(f"Preferred Location: {location}")
print(f"Fee Proof: {fee_proof}")
gather_course_details()