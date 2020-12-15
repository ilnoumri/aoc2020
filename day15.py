from lib import open_file
import sys
try:
    if sys.argv[1] == "--sample":
        numbers = open_file("15/15.sample")
    else:
        numbers = open_file("15/15.input")
except:
        numbers = open_file("15/15.input")

numbers = [int(elt) for elt in numbers[0].split(",")]


def run(numbers, limit=2020):
    numbers = numbers.copy()
    seen = {number: idx for idx, number in enumerate(numbers)}
    last_spoken = numbers[-1]
    for i in range(len(numbers)-1, limit-1):
        seen[last_spoken], last_spoken = i, i - seen[last_spoken] if last_spoken in seen else 0
    return last_spoken

print("### PART 1")
print(run(numbers))
print("### PART 2")
print(run(numbers, 30000000))
