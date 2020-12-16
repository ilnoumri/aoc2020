from lib import open_file
from functools import lru_cache
import sys
try:
    if sys.argv[1] == "--sample":
        info = open_file("16/sample")
    else:
        info = open_file("16/input")
except:
    info = open_file("16/input")
ranges = {}
idx = 0
while idx < len(info):
    if not info[idx]:
        idx += 2
        break
    line = info[idx]
    key, v = line.split(":")
    v = v.split("or")
    value = []
    for r in v:
        a, b = r.strip().split("-")
        a, b = int(a), int(b)
        value.append((a, b))
    ranges[key] = value
    idx += 1

my_ticket = [int(elt) for elt in info[idx].split(",")]
idx += 3
nearby_tickets = []
for i in range(idx, len(info)):
    nearby_tickets.append([int(elt) for elt in info[i].split(",")])


@lru_cache(maxsize=None)
def check_num_in_a_range(num):
    for v in ranges.values():
        for low, hi in v:
            if low <= num <= hi:
                return True
    return False


@lru_cache(maxsize=None)
def check_num_in_field_range(num, field):
    for low, hi in ranges[field]:
        if low <= num <= hi:
            return True
    return False


def find_correct_range(idx, correct_tickets):
    found = False
    possible_fields = []
    for field in ranges:
        for correct_ticket in correct_tickets:
            if not check_num_in_field_range(correct_ticket[idx], field):
                found = False
                break
            else:
                found = True
        if found:
            possible_fields.append(field)
    return possible_fields


def find_min_key_min_value(d):
    min_k = None
    min_v = []
    len_min_v = float("inf")
    for k, v in d.items():
        if len(v) < len_min_v:
            min_v = v
            min_k = k
            len_min_v = len(v)
    return min_k, min_v


def find_which_range(correct_tickets):
    # res will be a dict of field: [possible idx]
    res = {}
    for i in range(len(correct_tickets[0])):
        possible_fields = find_correct_range(i, correct_tickets)
        for p_f in possible_fields:
            if p_f not in res:
                res[p_f] = [i]
            else:
                res[p_f].append(i)
    all_attributed = False
    res_size = len(res.keys())
    # final_res will be a dict of field: correct idx
    final_res = {}
    while len(final_res.keys()) != res_size:
        min_k, min_v = find_min_key_min_value(res)
        if len(min_v) != 1:
            print(min_v)
            raise Exception("There is a problem with the input")
        final_res[min_k] = min_v[0]
        del res[min_k]
        for key, value in res.items():
            if min_v[0] in value:
                value.remove(min_v[0])
    return final_res


def part1():
    res = 0
    bad_nearby_tickets = []
    for nearby_ticket in nearby_tickets:
        for num in nearby_ticket:
            if not check_num_in_a_range(num):
                res += num
                bad_nearby_tickets.append(nearby_ticket)
    return res, bad_nearby_tickets


def part2(bad_nearby_tickets):
    correct_tickets = nearby_tickets
    for bad_nearby_ticket in bad_nearby_tickets:
        correct_tickets.remove(bad_nearby_ticket)
    fields = find_which_range(correct_tickets)
    res = 1
    for field in fields:
        if field.startswith("departure"):
            res *= my_ticket[fields[field]]
    return res


print("### PART 1")
part1_res, bad_nearby_tickets = part1()
print(part1_res)
print(part2(bad_nearby_tickets))
