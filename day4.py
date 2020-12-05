from lib import open_file
import re

_input = open_file("4/input")
# We add an ending empty string just for conveniance
_input.append("")
passports = []
passport = {}
for elt in _input:
    if elt:
        _elt = elt.split()
        for __elt in _elt:
            key, value = __elt.split(":")
            passport[key] = value
    else:
        passports.append(passport)
        passport = {}
required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
def digits_regstring(n=4, add=""):
    base = r"^[0-9]{" + str(n) + "}"
    if add:
        base += add
    return base + "$"

def digits_regexp(n=4, add=""):
    return re.compile(digits_regstring(n, add))

def byr(s):
    return digits_regexp().match(s) and int(s) >= 1920 and int(s) <= 2002

def iyr(s):
    return digits_regexp().match(s) and int(s) >= 2010 and int(s) <= 2020

def eyr(s):
    return digits_regexp().match(s) and int(s) >= 2020 and int(s) <= 2030

def hgt(s):
    if digits_regexp(3,"cm").match(s):
        num = s.strip("cm")
        return int(num) >= 150 and int(num) <= 193
    if digits_regexp(2, "in").match(s):
        num = s.strip("in")
        return int(num) >= 59 or int(num) <= 76
    return False

def hcl(s):
    return re.compile(r"^#([0-9]|[a-f]){6}$").match(s)

def ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid(s):
    return digits_regexp(9).match(s)

def valid_passport(passport,hard_check=False):
    if len(passport.keys()) < 7:
        return False
    for field in required_fields:
        if field not in passport.keys():
            return False
        if hard_check:
            arg = passport[field]
            call = f'{field}("{arg}")'
            if not eval(call):
                return False
    return True

def valid_passports(passports, hard_check=False):
    return sum(1 for passport in passports if valid_passport(passport, hard_check))

print("### PART 1")
print(valid_passports(passports))
    
print("### PART 2")
print(valid_passports(passports, hard_check=True))

