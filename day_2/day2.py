def find_evenly_divisible(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            temp = (li[i], li[j])
            big = max(temp)
            small = min(temp)
            if big // small == big / small:
                return big // small

def main():
    f = open('output.txt', 'r')
    line = f.readline()
    total = 0
    while(line):
        temp = [int(i) for i in line.split()]
        total += find_evenly_divisible(temp)
        line = f.readline()
    print(total)
if __name__ == "__main__":
    main()
