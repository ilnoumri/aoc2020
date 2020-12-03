def open_file(path):
    with open(path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
