def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    naughty = 0
    ranges_to_traverse = data[0].split(",")
    for range_to_traverse in ranges_to_traverse:
        range_list = range_to_traverse.split("-")
        start, stop = range_list[0], range_list[1]
        for i in range(int(start),int(stop) + 1):
            str_num = str(i)
            length = len(str_num)
            if str_num[:length//2] == str_num[length//2:]:
                naughty = naughty + i
    return naughty

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
