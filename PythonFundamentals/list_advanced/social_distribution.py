population = list(map(int, input().split(', ')))
population.sort()
min_wealth = int(input())
is_enough_wealth = True
last_element = len(population) -1

while max(population) > min_wealth and any(x for x in population if x < min_wealth):
    need_wealth = min_wealth - min(population)
    min_index = population.index(min(population))
    max_index = population.index(max(population))

    if need_wealth <= population[max_index]:
        population[max_index] -= need_wealth
        population[min_index] += need_wealth
    else:
        population[min_index] += population[min_index] - min_wealth
        population[min_index] = min_wealth

if all(x >= min_wealth for x in population):
    print(population)
else:
    print('No equal distribution possible')
