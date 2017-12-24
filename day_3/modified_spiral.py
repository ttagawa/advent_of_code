def get_current_number(spiral, row, column):
    total = 0
    total = try_adjacent(spiral, row-1, column-1, total)
    total = try_adjacent(spiral, row-1, column, total)
    total = try_adjacent(spiral, row-1, column+1, total)
    total = try_adjacent(spiral, row, column-1, total)
    total = try_adjacent(spiral, row, column+1, total)
    total = try_adjacent(spiral, row+1, column-1, total)
    total = try_adjacent(spiral, row+1, column, total)
    total = try_adjacent(spiral, row+1, column+1, total)
    return total

def try_adjacent(spiral, row, column, sum):
    try:
        if row < 0 or column < 0:
            return sum
        return sum + spiral[row][column]
    except:
        return sum

def go_right(spiral, curr):
    for i in range(len(spiral)):
        curr = get_current_number(spiral, len(spiral)-1, i+1)
        spiral[-1].append(curr)
    return curr

def go_up(spiral ,curr):
    for i in range(len(spiral)-1, -1, -1):
        curr = get_current_number(spiral, i, len(spiral[-1])-1)
        if i == 0:
            spiral.insert(i, [0 for j in range(len(spiral[-1]))])
            spiral[0][-1] = curr
        else:
            spiral[i-1].append(curr)
    return curr

def go_left(spiral,curr):
    for i in range(len(spiral)-2,-1,-1):
        curr = get_current_number(spiral, 0, i)
        spiral[0][i] = curr
    return curr

def go_down(spiral,curr):
    height = len(spiral)
    for i in range(height+1):
        curr = get_current_number(spiral, i, 0)
        if i == height:
            spiral.append([curr])
        else:
            spiral[i].insert(0, curr)
    return curr
def generate_spiral(n):
    spiral = [[1]]
    last = 0
    curr = 2
    while(curr <= n):
        curr = go_right(spiral,curr)
        curr = go_up(spiral,curr)
        curr = go_left(spiral, curr)
        curr = go_down(spiral, curr)
    return spiral

def print_spiral(spiral):
    for row in spiral:
        print(row)

if __name__ == '__main__':
    num = int(input("What is your input number?"))
    spiral = generate_spiral(num)
    print_spiral(spiral)
