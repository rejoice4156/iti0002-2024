"""School class which stores information about courses and students."""
from student import Student
from course import Course


class School:
    """School class, do not change."""

    def __init__(self, name):
        """School constructor."""
        self.name = name
        self.students = []
        self.courses = []
        self.__next_id = 1

    def add_course(self, course: Course):
        """Add a course."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """Add a student."""
        if student not in self.students:
            self.students.append(student)
            student.set_id(self.__next_id)
            self.__next_id += 1

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Add a student grade."""
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list[Student]:
        """Get all students."""
        return self.students

    def get_courses(self) -> list[Course]:
        """Get all courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """Get all students ordered by average grade."""
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
