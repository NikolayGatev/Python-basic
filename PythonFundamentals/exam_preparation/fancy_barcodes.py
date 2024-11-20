import re


count = int(input())
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])'

for _ in range(count):
    barcode = input()
    mach = re.match(pattern, barcode)
    if mach:
        core = mach.group(1)
        product_code = ''.join(filter(str.isdigit, core)) or '00'
        print(f'Product group: {product_code}')
    else:
        print('Invalid barcode')