from lib import open_file


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
def valid_passport(passport):
    if len(passport.keys()) < 7:
        return False
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True

def valid_passports(passports):
    return sum(1 for passport in passports if valid_passport(passport))

print("### PART 1")
print(valid_passports(passports))
    


