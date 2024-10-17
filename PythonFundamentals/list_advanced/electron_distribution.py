
electrons = int(input())

shells = []
shell = 0

while electrons > 0:
    shell += 1

    if shell ** 2 * 2 <= electrons:
        shells.append(shell ** 2 * 2)
        electrons -= shell ** 2 * 2
    else:
        shells.append(electrons)
        electrons = 0

print(shells)