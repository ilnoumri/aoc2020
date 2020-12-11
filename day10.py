from lib import open_file

nums = [int(n) for n in open_file("10/input")]
jolt_max = max(nums) + 3
nums.append(jolt_max)
nums.append(0)
nums.sort()


def find_jolt_diffs_nb(n, picked={}):
    nb = 0
    for num in nums:
        if num + n in nums:
            if num not in picked:
                nb += 1
                picked[num] = True
    return nb, picked


seen = {}


def distinct_arrangements_nb(jolt, jolt_low, jolt_hi):
    if jolt in seen:
        return seen[jolt]
    if jolt == jolt_max:
        seen[jolt] = 1
        return 1
    arrs = [elt for elt in nums if jolt_low <= elt - jolt <= jolt_hi]
    arrangements = 0
    for j in arrs:
        res = distinct_arrangements_nb(j, jolt_low, jolt_hi)
        seen[j] = res
        arrangements += res
    return arrangements


print("### PART 1")
jolt_1, picked = find_jolt_diffs_nb(1)
jolt_3, picked = find_jolt_diffs_nb(3, picked)
print(jolt_1 * jolt_3)
print("### PART 2")
print(distinct_arrangements_nb(0, 1, 3))
