from lib import open_file

instructions = open_file("8/input")


def run(instructions):
    seen = set()
    acc = 0
    idx = 0
    infinite_loop = False
    while idx < len(instructions):
        opcode, value = instructions[idx].split()
        if idx in seen:
            infinite_loop = True
            break
        else:
            seen.add(idx)
        if opcode == "nop":
            idx += 1
            continue
        value = int(value)
        if opcode == "acc":
            acc += value
            idx += 1
        if opcode == "jmp":
            idx += value
    return (acc, infinite_loop, seen)


def find_acc(instructions, autofix=False):
    ins = instructions.copy()
    acc, infinite_loop, seen = run(ins)
    if not autofix:
        return acc
    for idx in seen:
        opcode, value = instructions[idx].split()
        if opcode not in ("jmp", "nop"):
            continue
        if opcode == "jmp":
            ins[idx] = f"nop {value}"
        else:
            ins[idx] = f"jmp {value}"
        acc, infinite_loop, seen = run(ins)
        if infinite_loop:
            ins = instructions.copy()
        else:
            print(
                f"Autofix successful! Error was {opcode} {value} at index {idx}")
            return acc
    print("Could not fix the instructions set")
    return None


print("### PART 1")
print(find_acc(instructions))
print("### PART 2")
print(find_acc(instructions, autofix=True))
