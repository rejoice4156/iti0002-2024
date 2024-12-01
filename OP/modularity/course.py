"""Course class with name and grades."""


class Course:
    """Course class, do not change."""

    def __init__(self, name: str):
        """Course constructor."""
        self.name = name
        self.grades = []

    def add_grade(self, student, grade: float):
        """Add a grade to the course."""
        self.grades.append((student, grade))

    def get_grades(self) -> list[tuple[str, int]]:
        """Get grades."""
        return self.grades

    def get_average_grade(self) -> float:
        """Get average grade."""
        if self.grades:
            sum_of_all_grades = sum(grade for _, grade in self.grades)
            return sum_of_all_grades / len(self.grades)
        return -1

    def __repr__(self):
        """Get string representation of course name."""
        return f"{self.name}"
