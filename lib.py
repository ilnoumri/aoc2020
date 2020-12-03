def open_file(path):
    with open(path) as f:
        lines = f.readlines()
    return lines
