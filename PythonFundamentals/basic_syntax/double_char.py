from cgitb import strong

string = input()
while string != 'End':
    if string == 'SoftUni':
        string = input()
        continue
    for i in string[:: 1]:
        print(2 * i, end = "")
    print()
    string = input()