from lib import open_file
from copy import deepcopy
seats = [list(elt) for elt in open_file("11/input")]


def get_adjeacents(x, y):
    return ((x, y+1), (x+1, y), (x, y-1), (x-1, y), (x-1, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1))


def check_adj_occupied1(x, y, seats):
    '''
    Return True when there is 4+ occupied adjeaceant seat around occupied
    seat(x,y)
    '''
    adjeacents = get_adjeacents(x, y)
    occupied = 0
    for seat in adjeacents:
        x, y = seat
        if x < 0 or y < 0 or x >= len(seats) or y >= len(seats[0]):
            continue
        if seats[x][y] == "#":
            occupied += 1
    return occupied


def check_adj_occupied2(x, y, seats):
    '''
    Return True when there is 5+ occupied adjeaceant seat around occupied
    seat(x,y)
    '''
    adjeacents = get_adjeacents(x, y)
    occupied = 0
    for i in range(len(adjeacents)):
        x_, y_ = adjeacents[i]
        while True:
            if x_ < 0 or y_ < 0 or x_ >= len(seats) or y_ >= len(seats[0]):
                break
            if seats[x_][y_] == "#":
                occupied += 1
                break
            elif seats[x_][y_] == "L":
                break
            x_, y_ = get_adjeacents(x_, y_)[i]
    return occupied


def check_adj_occupied(x, y, seats, new_check=False):
    if new_check:
        return check_adj_occupied2(x, y, seats)
    return check_adj_occupied1(x, y, seats)


def count_occupied_seats(seats):
    return sum(1 for seat in seats for s in seat if s == "#")


def pprint(seats):
    for seat in seats:
        print("".join(seat))


def apply_rules(seats_=None, limit=4, new_check=False):
    changes = False
    if not seats_:
        seats_ = deepcopy(seats)
    base = deepcopy(seats_)
    for i in range(len(seats_)):
        for j in range(len(seats_[0])):
            occupied = check_adj_occupied(i, j, base, new_check)
            if seats_[i][j] == "L" and occupied == 0:
                seats_[i][j] = "#"
                changes = True
            elif seats_[i][j] == "#" and occupied >= limit:
                seats_[i][j] = "L"
                changes = True
    return changes, seats_


print("### PART 1")
changes, seats_ = apply_rules()
while changes:
    changes, seats_ = apply_rules(seats_)
print(count_occupied_seats(seats_))

print("### PART 2")
changes, seats_ = apply_rules(seats_=None, limit=5, new_check=True)
while changes:
    changes, seats_ = apply_rules(seats_, limit=5, new_check=True)
print(count_occupied_seats(seats_))
