def go_right(spiral, curr):
    for i in range(len(spiral)):
        spiral[-1].append(curr)
        curr += 1
    return curr

def go_up(spiral, curr):
    for i in range(len(spiral)-1, -1, -1):
        if i == 0:
            spiral.insert(i, [])
            spiral[0].append(curr)
        else:
            spiral[i-1].append(curr)
        curr += 1
    return curr

def go_left(spiral, curr):
    for i in range(len(spiral)):
        spiral[0].insert(0,curr)
        curr += 1
    return curr

def go_down(spiral, curr):
    for i in range(len(spiral)):
        if i == len(spiral) - 1:
            spiral.append([])
        spiral[i+1].insert(0, curr)
        curr += 1
    return curr
def generate_spiral(n):
    spiral = [[1]]
    curr = 2
    while(curr <= n):
        curr = go_right(spiral, curr)
        curr = go_up(spiral, curr)
        curr = go_left(spiral, curr)
        curr = go_down(spiral, curr)
    return spiral

def print_spiral(spiral):
    for row in spiral:
        print(row)

if __name__ == '__main__':
    spiral = generate_spiral(20)
    print_spiral(spiral)
