class Student:
    def __init__(self, id, name, mathScore, chemistryScore, literatureScore):
        self.id = id
        self.name = name
        self.mathScore = mathScore
        self.chemistryScore = chemistryScore
        self.literatureScore = literatureScore

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_math_score(self):
        return self.mathScore

    def get_chemistry_score(self):
        return self.chemistryScore

    def get_literature_score(self):
        return self.literatureScore

    def get_average(self):
        return (self.mathScore + self.chemistryScore + self.literatureScore) / 3

def main():
    listStudent = []
    student1 = Student(0, f'Student A', 10, 8, 6)
    student2 = Student(1, f'Student B', 1, 4, 5)
    student3 = Student(2, f'Student C', 2, 9, 10)
    student4 = Student(3, f'Student D', 3, 7, 8)
    student5 = Student(4, f'Student E', 4, 9, 9)

    listStudent.append(student1)
    listStudent.append(student2)
    listStudent.append(student3)
    listStudent.append(student4)
    listStudent.append(student5)

    list_student_with_average_greater_5 = [student for student in listStudent if student.get_average() > 5]
    print("Sinh vien co diem trung binh lon hon 5")
    for student in list_student_with_average_greater_5:
        print(f"{student.get_name()}, {student.get_average()}")

    print("Sinh vien co diem hoa nho hon 5")
    list_student_with_chemistry = [student for student in listStudent if student.get_chemistry_score() < 5]
    for student in list_student_with_chemistry:
        print(f"{student.get_name()}, {student.get_chemistry_score()}")



if __name__ == "__main__":
    main()