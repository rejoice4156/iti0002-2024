"""Student class with student name and grades."""


class Student:
    """Student class, do not change."""

    def __init__(self, name: str):
        """Student constructor."""
        self.name = name
        self.grades = []
        self.id = None

    def set_id(self, id: int):
        """Set id for student."""
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        """Get id for student."""
        return self.id

    def add_grade(self, course, grade: int):
        """Add grade for student."""
        self.grades.append((course, grade))

    def get_grades(self) -> list[tuple[str, int]]:
        """Get grades for student."""
        return self.grades

    def get_average_grade(self):
        """Get average grade for student."""
        if self.grades:
            sum_of_all_grades = 0
            for _, grade in self.grades:
                sum_of_all_grades += grade
            return sum_of_all_grades / len(self.grades)
        return -1

    def __repr__(self) -> str:
        """Get string representation of student name."""
        return f"{self.name}"
