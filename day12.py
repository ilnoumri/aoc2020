from lib import open_file
import sys
try:
    if sys.argv[1] == "--sample":
        instructions = open_file("12/sample")
except:
    instructions = open_file("12/input")

directions = ("E", "S", "W", "N")
current = {"E": 0, "N": 0}
facing = {"value": "E", "opposite": "W", "idx": 0}
waypoint = {"E": 10, "N": 1}
current_waypoint = {"E": 0, "N": 0}
waypoint_dirs = ("EN", "ES", "WS", "WN")


def manhattan_distance(current):
    res = 0
    for v in current.values():
        res += abs(v)
    return res

def move(direction, value, current_=current):
    to_add = value
    dir_idx = directions.index(direction)
    opposite = directions[(dir_idx+2)%4]
    if opposite in current_:
        if current_[opposite] - value > 0:
            final_direction = opposite
            to_add = current_[opposite] - value
        else:
            final_direction = direction
            to_add = value - current_[opposite]
        del current_[opposite]
        current_[final_direction] = to_add
    elif direction in current_:
        current_[direction] += value
    else:
        current_[direction] = value

def forward(value):
    to_add = value
    opposite = facing["opposite"]
    if opposite in current:
        if to_add - current[opposite] > 0:
            final_direction = facing["value"]
            to_add -= current[opposite]
        else:
            final_direction = opposite
            to_add = current[opposite] - to_add
        del current[opposite]
        current[final_direction] = to_add
    elif facing["value"] in current:
        current[facing["value"]] += to_add
    else:
        current[facing["value"]] = to_add

def forward_waypoint(value):
    to_add = {}
    for k,v in waypoint.items():
        to_add[k] = value * v
    for k,v in to_add.items():
        move(k, v, current_waypoint)


def turn(direction, value):
    possibilities = {90: 1, 180: 2, 270: 3}
    new_dir_idx = (facing["idx"]  + possibilities[value]) % 4
    if direction == "L":
        new_dir_idx = (facing["idx"] - possibilities[value]) % 4
    facing["value"] = directions[new_dir_idx]
    facing["opposite"] = directions[(new_dir_idx+2)%4]
    facing["idx"] = new_dir_idx

def swap(d, a, b):
    tmp = d[b] 
    d[b] = d[a]
    d[a] = tmp

def turn_waypoint(direction, value):
    global waypoint
    possibilities = {90: 1, 180: 2, 270: 3}
    waypoint_keys = list(waypoint.keys())
    if waypoint_keys[0] not in "EW":
        swap(waypoint_keys, 0, 1)
    position = "".join(waypoint_keys)
    waypoint_idx = waypoint_dirs.index(position)
    new_waypoint = waypoint_dirs[(waypoint_idx + possibilities[value])%4]
    if direction == "L":
        new_waypoint = waypoint_dirs[(waypoint_idx - possibilities[value])%4]
    old = waypoint
    waypoint = {}
    for direction in list(new_waypoint):
        if direction in "EW":
            if "E" in old:
                waypoint[direction] = old["E"]
            else:
                waypoint[direction] = old["W"]
        elif direction in "NS":
            if "N" in old:
                waypoint[direction] = old["N"]
            else:
                waypoint[direction] = old["S"]
    if possibilities[value] != 2:
        keys = list(waypoint.keys())
        swap(waypoint, keys[0], keys[1])
 
def apply_inst():
    for ins in instructions:
        i = list(ins)
        direction, value = i[0], int("".join(i[1:]))
        if direction == "F":
            forward(value)
            forward_waypoint(value)
        elif direction in "LR":
            turn(direction, value)
            turn_waypoint(direction, value)
        elif direction in "NSEW":
            move(direction, value)
            move(direction, value, waypoint)

apply_inst()
print("### PART 1")
print(manhattan_distance(current))

print("### PART 2")
print(manhattan_distance(current_waypoint))
