courses = {}

while True:

    token = input().split(' : ')
    if len(token) == 1:
        break
    course = token[0]
    student = token[1]
    if course not in courses.keys():
        courses[course] = []
    if student not in courses[course]:
        courses[course].append(student)
courses = dict(sorted(courses.items(), key=lambda item: len(item[1]), reverse=False))
for item in courses.items():
    print(f"{item[0]}: {len(item[1])}\n-- {str.join('\n-- ', item[1])}")