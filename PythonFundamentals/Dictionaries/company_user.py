companies = {}

while True:
    token = input().split(' -> ')
    if len(token) == 1:
        break
    company = token[0]
    employee = token[1]

    if company not in companies.keys():
        companies[company] = set()

    companies[company].add(employee)

for item in companies.items():
    print(item[0])
    for x in item[1]:
        print(f"-- {x}")