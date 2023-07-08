def avg(values):
    return sum(values) / len(values)


n = int(input())

students = {}

for i in range(n):
    data = input().split()
    name = data[0]
    grade = float(data[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)


for student, grades in students.items():
    grates_formatted = " ".join(f'{grade:.2f}' for grade in grades)
    average_grade = avg(grades)
    print(f"{student} -> {grates_formatted} (avg: {average_grade:.2f})")
