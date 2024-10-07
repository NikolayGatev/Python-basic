
def tribonacci_sequence(x1:int) -> []:
    result = []
    for x in range(1,x1 +1):
       if x <= 2:
           result.append(1)
       elif x == 3:
           result.append(2)
       else:
           result.append(sum(result[-3:]))

    return result

x1 = int(input())


print(f'{str.join(' ',str(tribonacci_sequence(x1)))}')