ls = []

class Student:
    def __init__(self, name, rollno, marks_1, marks_2):
        self.name = name
        self.rollno = rollno
        self.marks_1 = marks_1
        self.marks_2 = marks_2

def onboard_student(name, rollno, marks_1, marks_2):
    obj = Student(name, rollno, marks_1, marks_2)
    ls.append(obj)

def display_student(obj):
    print("Name: ", obj.name)
    print("Roll No: ", obj.rollno)
    print("Marks 1: ", obj.marks_1)
    print("Marks 2: ", obj.marks_2, "\n")

def search(rollno):
    for student in ls:
        if student.rollno == rollno:
            return student
    return None

def delete(rollno):
    student = search(rollno)
    if student:
        ls.remove(student)
        print(f"Student with roll number {rollno} has been deleted.")
    else:
        print(f"Student with roll number {rollno} not found.")

def update_student(rollno, name=None, marks_1=None, marks_2=None):
    student = search(rollno)
    if student:
        if name:
            student.name = name
        if marks_1 is not None:
            student.marks_1 = marks_1
        if marks_2 is not None:
            student.marks_2 = marks_2
        print(f"Student with roll number {rollno} has been updated.")
    else:
        print(f"Student with roll number {rollno} not found.")

# ONBOARD STUDENT
onboard_student("Jubayer", 1, 85, 80)
onboard_student("Abir", 2, 76, 86)
onboard_student("Mead", 3, 70, 75)

# DISPLAY ALL STUDENTS
print("------------------------------------------")
for student in ls:
    display_student(student)
print("------------------------------------------")

# SEARCH STUDENT
print("------------------------------------------")
student = search(1)
if student:
    print("Student Found")
    display_student(student)
else:
    print("Student Not Found")
print("------------------------------------------")

# DELETE STUDENT
print("------------------------------------------")
delete(2)
print("------------------------------------------")

# DISPLAY ALL STUDENTS AFTER DELETION
print("------------------------------------------")
for student in ls:
    display_student(student)
print("------------------------------------------")

# UPDATE STUDENT
print("------------------------------------------")
update_student(1, name="Jubayer Rahman", marks_1=90, marks_2=85)
print("------------------------------------------")

# DISPLAY ALL STUDENTS AFTER UPDATE
print("------------------------------------------")
for student in ls:
    display_student(student)
print("------------------------------------------")
