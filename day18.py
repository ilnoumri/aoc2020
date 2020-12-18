from lib import open_file
import sys
import re
try:
    if sys.argv[1] == "--sample":
        exps = open_file("18/sample")
    else:
        exps = open_file("18/input")
except:
    exps = open_file("18/input")


def get_parenthesis(exp):
    ps = ""
    insert = False
    for e in exp:
        if e == "(":
            if insert:
                ps = ""
                continue
            insert = True
        elif e == ")":
            return ps
        elif insert:
            ps += e
    return ps

def replace_parenthesis(exp, addition_first=False):
    parenthesis = get_parenthesis(exp)
    while parenthesis:
        parenthesis_res = compute(parenthesis, addition_first)
        exp = exp.replace(f"({parenthesis})", str(parenthesis_res))
        parenthesis = get_parenthesis(exp)
    return exp

def replace_addition(exp):
    if "(" not in exp and "*" not in exp:
        return str(compute(exp))
    addition = re.search("\d+ \+ \d+", exp)
    while addition:
        addition_res = compute(addition.group())
        exp = exp.replace(addition.group(), str(addition_res), 1)
        addition = re.search("\d+ \+ \d+", exp)
    return exp

def compute(exp, addition_first=False):
    if "(" in exp:
        exp = replace_parenthesis(exp, addition_first)
    if addition_first:
        exp = replace_addition(exp)
    exp = [int(e) if e.isnumeric() else e for e in exp.split()]
    res = 0
    i = 0
    while i < len(exp):
        if exp[i] == "+":
            res += exp[i+1]
            i += 2
        elif exp[i] == "*":
            res *= exp[i+1]
            i += 2
        else:
            res = exp[i]
            i += 1
    return res

def part1():
    res = []
    for exp in exps:
        res.append(compute(exp))
    return sum(e for e in res)

def part2():
    res = []
    for exp in exps:
        res.append(compute(exp, addition_first=True))
    return sum(e for e in res)


print("### PART 1")
print(part1())

print("### PART 2")
print(part2())
