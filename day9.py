from lib import open_file

numbers = open_file("9/input")
numbers = [int(num) for num in numbers]

def property_checker(preamble, nb):
    for elt in preamble:
        if nb-elt in preamble:
            return True
    return False

def find_nb_not_matching(n):
    idx = 0
    while idx < len(numbers):
        preamble = set(numbers[idx:idx+n])
        nb = numbers[idx + n]
        if not property_checker(preamble, nb):
            return nb, idx+n
        idx += 1

def find_encryption_weakness():
    target, idx = find_nb_not_matching(25)
    candidate_nbs = set()
    i = idx-1
    cursor = i
    while 0 < i:
        candidate_res = sum(nb for nb in candidate_nbs)
        if candidate_res == target:
            return max(candidate_nbs) + min(candidate_nbs)
        if candidate_res > target:
            candidate_nbs = set()
            cursor -= 1
            i = cursor
        else:
            candidate_nbs.add(numbers[i])
            i-=1

    
print("### PART 1")
print(find_nb_not_matching(25)[0])
print("### PART 2")
print(find_encryption_weakness())
