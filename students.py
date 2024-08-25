students = [
    {
        "id": 1,
        "name": "Nguyen Van A",
        "mathScore": 5,
        "chemistryScore": 4,
        "literatureScore": 3,
    },
    {
        "id": 2,
        "name": "Nguyen Van B",
        "mathScore": 9,
        "chemistryScore": 8,
        "literatureScore": 9,
    },
    {
        "id": 3,
        "name": "Nguyen Van C",
        "mathScore": 1,
        "chemistryScore": 1,
        "literatureScore": 2,
    },
    {
        "id": 4,
        "name": "Nguyen Van D",
        "mathScore": 5,
        "chemistryScore": 6,
        "literatureScore": 5,
    },
    {
        "id": 5,
        "name": "Nguyen Van E",
        "mathScore": 10,
        "chemistryScore": 0,
        "literatureScore": 1,
    }
]

list_student_with_average_greater_5 = [student for student in students if (student["mathScore"] + student["chemistryScore"] + student["literatureScore"])/3 >5 ]
list_student_with_chemistry_less_than_or_equal_5 = [student for student in students if student["chemistryScore"]  <= 5 ]

print(list_student_with_average_greater_5)
print(list_student_with_chemistry_less_than_or_equal_5)