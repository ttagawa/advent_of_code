from spiral_generator import generate_spiral, print_spiral

def manhattan_distance(number):
    spiral = generate_spiral(number)
    for i in range(len(spiral)):
        try:
            col = spiral[i].index(number)
        except:
            continue
        else:
            index = (i, col)
            break
    mid = len(spiral) // 2
    ind_of_1 = (mid, mid)
    dist = 0
    for i in range(2):
        dist += abs(index[i] - ind_of_1[i])
    return dist, spiral

if __name__ == '__main__':
    print("Hi. This program will calculate the manhattan distance for a specified number and 1 in a spiral matrix.\n")
    num = int(input("What number do you want the manhattan distance of?"))
    dist, spiral = manhattan_distance(num)
    print_spiral(spiral)
    print("The manhattan distance is {}".format(dist))
