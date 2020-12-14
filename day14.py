from lib import open_file
from itertools import product
instructions = open_file("14/input")

memory = {}
memory2 = {}

def apply_mask(value, mask):
    res = ""
    for i in range(len(mask)):
        if mask[i] != "X":
            if mask[i] != value[i]:
                res += mask[i]
            else:
                res += value[i]
        else:
            res += value[i]
    return res

def get_bin_possibilities(num):
    return ["".join(comb) for comb in product(["0", "1"], repeat=num)]

def get_mask_possibilities(address, mask):
    res = ""
    for i in range(len(mask)):
        if mask[i] != '0':
            res += mask[i]
        else:
            res += address[i]
    num_X = res.count("X")
    bin_possibilities = get_bin_possibilities(num_X)
    addresses_to_insert = []
    for possibility in bin_possibilities:
        address_bin = ""
        idx_possibility = 0
        for i in range(len(res)):
            if res[i] == "X":
                address_bin += possibility[idx_possibility]
                idx_possibility += 1
            else:
                address_bin += res[i]
        addresses_to_insert.append(int(address_bin, 2))
    return addresses_to_insert

def insert_in_memory(address, value, mask):
    value = int(value)
    bin_format = '{' + f"0:0{len(mask)}b" + '}'
    binary = bin_format.format(value)
    result = apply_mask(binary, mask)
    memory[address] = int(result, 2)
    
def insert_in_memory_with_bitmask(address, value, bitmask):
    value = int(value)
    bin_format = '{' + f"0:0{len(bitmask)}b" + '}'
    binary = bin_format.format(address)
    addresses_to_insert = get_mask_possibilities(binary, bitmask)
    for a in addresses_to_insert:
        memory2[a] = value

def part1_part2():
    mask = None
    bitmask = None
    for instruction in instructions:
        key, value = [elt.strip() for elt in instruction.split("=")]
        if key == "mask":
            mask = value
            bitmask = value
        elif "mem" in key:
            begin, end = key.index("["), key.index("]")
            address = int(key[begin+1:end])
            insert_in_memory(address, value, mask)
            insert_in_memory_with_bitmask(address, value, mask)
    res1, res2 = 0, 0
    for v in memory.values():
        res1 += v
    for v in memory2.values():
        res2 += v
    return res1, res2

part1, part2 = part1_part2()
print("### PART 1")
print(part1)

print("### PART 2")
print(part2)
