from lib import open_file

seats = open_file("5/input")


def get_lower_bound_from_code(upp, code, symbol_low):
    low, upp = 0, upp
    for elt in code:
        if elt == symbol_low:
            upp = (upp+low)//2
        else:
            low = (upp+low+1)//2
    return low


def get_row(row_code):
    return get_lower_bound_from_code(127, row_code, 'F')


def get_column(column_code):
    return get_lower_bound_from_code(7, column_code, 'L')


def get_info(code):
    row = get_row(code[:7])
    column = get_column(code[7:])
    seat_id = row * 8 + column
    return (row, column, seat_id)


seats_info = [get_info(seat) for seat in seats]
print("### PART 1")
print(max([info[2] for info in seats_info]))

print("### PART 2")
seats_to_check = []
for seat_info in seats_info:
    if seat_info[0] == 0 or seat_info[0] == 127:
        continue
    seats_to_check.append(seat_info)

seats_to_check_ids = [info[2] for info in seats_to_check]
seats_to_check_ids.sort()
to_check = set(seats_to_check_ids)
range_to_check = range(seats_to_check_ids[0], seats_to_check_ids[-1] + 1)
res = None
for elt in range_to_check:
    if elt not in to_check:
        res = elt
        break
print(res)
