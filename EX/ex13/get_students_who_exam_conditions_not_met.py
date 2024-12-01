"""Get students who's exam conditions are not met."""


def get_students_who_exam_conditions_not_met(names1: list, names2: list) -> set:
    """
    To get to the exam, a person has to pass two tests.

    The first list passed as the function's argument contains the names of the people who passed the first test
    and the second list contains the names of the people who passed the second test.

    The function returns a set of names of the people who cannot take the exam.

    No loops required.

    get_students_who_exam_conditions_not_met(["Mati"], ["Mati", "Kati"]) => {"Kati"}
    get_students_who_exam_conditions_not_met(["Mati", "Kati"], ["Mati", "Kati"]) => {}
    get_students_who_exam_conditions_not_met(["Mati", "Kaja"], ["Mati", "Kati"]) => {"Kaja", "Kati"}
    """
    return set(names1) ^ set(names2)


if __name__ == "main":
    # run this file to test the function
    print(get_students_who_exam_conditions_not_met(["Mati"], ["Mati", "Kati"]))  # {"Kati"}
    print(get_students_who_exam_conditions_not_met(["Mati", "Kaja"], ["Mati", "Kati"]))
    # {"Kaja", "Kati"}
