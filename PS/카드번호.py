import re
card = input()
try:
    if card[0] not in ['4','5','6']:
        print("Invalid")
    elif re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', card):
        print("Valid")
except IndexError:
    print("Invalid")