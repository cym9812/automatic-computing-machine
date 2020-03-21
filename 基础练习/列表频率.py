def frequency(students):
    students_frequency = {}
    for name in students:
        students_frequency[name] = students.count(name)
    return students_frequency
