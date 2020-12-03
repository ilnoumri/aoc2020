from lib import open_file

lines = open_file("3/input")

_map = []
for line in lines:
    __map = []
    for square in line:
        __map.append(square)
    _map.append(__map)

def countTrees(right, down):
    map_width = len(_map[0])
    map_height = len(_map)
    cur_y = down
    cur_x = (0 + right) % (map_width)
    trees = 0
    while cur_y < map_height:
        if _map[cur_y][cur_x] == "#":
            trees += 1
        cur_x = (cur_x + right) % (map_width)
        cur_y = cur_y + down
    return trees

print("### PART 1")
print(countTrees(3, 1))
dirs = [(1,1), (3,1), (5,1), (7,1), (1,2)]
res = 1
for d in dirs:
    right, down = d
    res *= countTrees(right, down)

print("### PART 2")
print(res)

