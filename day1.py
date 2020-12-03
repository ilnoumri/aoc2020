from lib import open_file
s = set()
s2 = []
lines = open_file("1/input")
for line in lines:
    num = int(line.strip())
    s.add(num)
    s2.append(num) 
def find_two_numbers():
    for e in s2:
        if 2020-e in s:
            return (e, 2020-e)
        
def find_three_numbers():
    for i in range(len(s2)):
        for j in range(len(s2)):
            if 2020 - s2[i] - s2[j] in s:
                return (s2[i], s2[j], 2020 - s2[i] - s2[j])
a, b = find_two_numbers()
print("### PART 1")
print(a*b)
a, b, c = find_three_numbers()
print("### PART 2")
print(a*b*c)

