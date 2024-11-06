countries = input().split(', ')
capitals = input().split(', ')
information = {countries[index]: capitals[index] for index in range(len(countries))} # dictionary comprehension

for item in information.items():
    print(f"{item[0]} -> {item[1]}")

dict_information = dict(zip(countries, capitals)) # generate dict with zip