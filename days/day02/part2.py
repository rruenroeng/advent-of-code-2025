def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def is_invalid(str_num:str) -> bool:
    length = len(str_num)
    for j in range(1,length):
        sequence_to_find = str_num[:j]
        # print(sequence_to_find)
        # print(sequence_to_find*(length//j))
        # print(str_num)
        # print()
        if sequence_to_find*(length//j) == str_num:
            # print(str_num)
            return True
    return False

def solve(data):
    naughty = 0
    ranges_to_traverse = data[0].split(",")
    for range_to_traverse in ranges_to_traverse:
        range_list = range_to_traverse.split("-")
        start, stop = range_list[0], range_list[1]
        for i in range(int(start),int(stop) + 1):
            str_num = str(i)
            if is_invalid(str_num):
                naughty = naughty + i
    return naughty

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))

# Two new edge cases to handle 