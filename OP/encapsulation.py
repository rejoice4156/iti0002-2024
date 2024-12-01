"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name: str, id: int):
        """Student constructor."""
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        """Get student id."""
        return self.__id

    def set_name(self, name: str):
        """Set student name."""
        self.__name = name

    def get_name(self):
        """Get student name."""
        return self.__name

    def set_status(self, status: str):
        """Set student status."""
        valid_statuses = ["Active", "Expelled", "Finished", "Inactive"]
        if status in valid_statuses:
            self.__status = status

    def get_status(self):
        """Get student status."""
        return self.__status
