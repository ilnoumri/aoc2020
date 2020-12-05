from lib import open_file
import re

f = open_file("4/input")
# We add an ending empty string just for conveniance
f.append("")
passports = []
passport = {}
for elt in f:
    if elt:
        passport_elts = elt.split()
        for passport_elt in passport_elts:
            key, value = passport_elt.split(":")
            passport[key] = str(value)
    else:
        passports.append(passport)
        passport = {}

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
ecl_possibilities = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def digits_regstring(n=4, add=""):
    base = r"^[0-9]{" + str(n) + "}"
    if add:
        base += add
    return base + "$"


def digits_regexp(n=4, add=""):
    return re.compile(digits_regstring(n, add))


class Checker():
    def byr(self, s):
        return digits_regexp().match(s) and int(s) >= 1920 and int(s) <= 2002

    def iyr(self, s):
        return digits_regexp().match(s) and int(s) >= 2010 and int(s) <= 2020

    def eyr(self, s):
        return digits_regexp().match(s) and int(s) >= 2020 and int(s) <= 2030

    def hgt(self, s):
        if digits_regexp(3, "cm").match(s):
            num = s.strip("cm")
            return int(num) >= 150 and int(num) <= 193
        if digits_regexp(2, "in").match(s):
            num = s.strip("in")
            return int(num) >= 59 or int(num) <= 76
        return False

    def hcl(self, s):
        return re.compile(r"^#([0-9]|[a-f]){6}$").match(s)

    def ecl(self, s):
        return s in ecl_possibilities

    def pid(self, s):
        return digits_regexp(9).match(s)


checker = Checker()


def valid_passport(passport, hard_check=False):
    if len(passport.keys()) < 7:
        return False
    for field in required_fields:
        if field not in passport.keys():
            return False
        if hard_check:
            arg = passport[field]
            if not checker.__getattribute__(field)(arg):
                return False
    return True


def valid_passports(passports, hard_check=False):
    return sum(1 for passport in passports if valid_passport(passport, hard_check))


print("### PART 1")
print(valid_passports(passports))

print("### PART 2")
print(valid_passports(passports, hard_check=True))
