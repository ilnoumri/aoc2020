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
