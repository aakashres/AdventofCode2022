import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def is_greater_or_equal(x, y, rows, direction):
    val = rows[x][y]
    while True:
        if direction == "up":
            x, y = x-1, y
        if direction == "down":
            x, y = x+1, y
        if direction == "left":
            x, y = x, y-1
        if direction == "right":
            x, y = x, y+1
        if x < 0 or y < 0 or x >= len(rows) or y >= len(rows[0]):
            return True
        else:
            next_val = rows[x][y]
        if val <= next_val:
            return False
    



def main():
    input_file_path = os.path.join(current_dir, "input.test")
    _input = open("input8.txt", "r").read()
    rows = _input.split("\n")
    number_of_rows = len(rows)
    number_of_columns = len(rows[0])

    total_visible = set()
    for i, row in enumerate(rows):
        for j, elem in enumerate(row):
            if i == 0 or i == number_of_rows - 1:
                total_visible.add((i, j))
                continue
            elif j == 0 or j == number_of_columns - 1:
                total_visible.add((i, j))
                continue
            else:
                if is_greater_or_equal(i, j, rows, "up"):
                    total_visible.add((i, j))
                    continue
                if is_greater_or_equal(i, j, rows, "down"):
                    total_visible.add((i, j))
                    continue
                if is_greater_or_equal(i, j, rows, "left"):
                    total_visible.add((i, j))
                    continue
                if is_greater_or_equal(i, j, rows, "right"):
                    total_visible.add((i, j))
                    continue
    print(len(total_visible))
    for i, row in enumerate(rows):
        s = ""
        for j, elem in enumerate(row):
            if (i,j) in total_visible:
                s +=  f"  v({elem})) "
            else:
                s +=  f"  nv({elem})) "
                

if __name__ == "__main__":
    main()