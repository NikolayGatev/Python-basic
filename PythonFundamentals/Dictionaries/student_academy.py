from statistics import mean

students = {}
rows = int(input())

for x in range(rows):
    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

students = {item[0]: mean(item[1]) for item in students.items() if mean(item[1]) >= 4.5}
for item in students.items():
    print(f"{item[0]} -> {item[1]:.2f}")