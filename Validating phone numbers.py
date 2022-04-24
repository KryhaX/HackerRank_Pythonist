import re
quantity = int(input("Quantity : "))
check_validation = None
for n in range(1,quantity+1):
    check_validation = str(input(f"[{n}]Phone number: "))

if len(check_validation) <= 15 and len(check_validation) >= 2:
    print('YES' if re.search(r'^[7-9]',check_validation) else 'NO')

# Oneline
