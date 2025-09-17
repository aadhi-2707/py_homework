frontend_students = {"Adithyan", "Ashik", "Vishnu", "Akhil"}
backend_students = {"Faris", "Salman", "Vishnu", "Nithin"}
#  Adding a new student to the Backend course
backend_students.add("Hari")

#  Removing a student from the Frontend course
frontend_students.discard("Akhil")
#  Students  in both courses
both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)
#  Students only in Backend, not in Frontend
only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)
#  Total number of unique students
unique_students = frontend_students | backend_students
print("Total unique students:", len(unique_students))
#  Dictionary with course names and student counts
course_enrollments = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
# Print each course name with number of students
for course, count in course_enrollments.items():
    print(f"{course}: {count} students")
   
    fullstack_enrollments = {
    **course_enrollments,
    "Fullstack": len(frontend_students & backend_students)
}
print("Course enrollments including Fullstack:", fullstack_enrollments)


