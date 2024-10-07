
def password_validator(a: str) -> []:
    result = []
    if not (6 <= len(a) <= 10):
        result.append('Password must be between 6 and 10 characters')
    if not str.isalnum(a):
        result.append('Password must consist only of letters and digits')
    if len([x for x in a if str.isdigit(x)]) < 2:
        result.append('Password must have at least 2 digits')

    return ['Password is valid'] if not result else result

password = input()

print(str.join('\n',password_validator(password)))