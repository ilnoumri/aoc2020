from lib import open_file

def policy_splitter(policy):
    _range, letter = policy.split()
    low, upp = _range.split("-")
    low, upp = int(low), int(upp)
    return (low, upp, letter)

def check(policy, password):
    low, upp, letter = policy_splitter(policy)
    occ = password.count(letter)
    if occ >= low and occ <= upp:
        return True
    return False

def new_check(policy, password):
    low, upp, letter = policy_splitter(policy)
    return (password[low] == letter) ^ (password[upp] == letter)

lines = open_file("2/input")
# PART 1
res = 0
for line in lines:
    policy, password = line.split(":")
    if check(policy, password):
        res += 1
print(f"### Part1")
print(res)

# PART 2
res = 0
for line in lines:
    policy, password = line.split(":")
    if new_check(policy, password):
        res += 1
print(f"### Part 2")
print(res)

