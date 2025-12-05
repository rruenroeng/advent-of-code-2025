def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def find_greatest(line: str, start: int, end: int):
    max_val = -1
    max_ind = -1

    # Walk backwards: start → end (inclusive)
    for i in range(start, end - 1):
        val = int(line[i])
        if val > max_val:
            max_val = val
            max_ind = i

    return max_val, max_ind

def solve(data):
    total_joltage = 0
    for line in data:
        line = str(line)
        max_left_val, max_left_ind = find_greatest(line, 0, len(line))
        max_right_val, _ = find_greatest(line, max_left_ind + 1, len(line)+1)
        print(int(str(max_left_val)+str(max_right_val)))
        total_joltage = total_joltage + int(str(max_left_val)+str(max_right_val))
    return total_joltage

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
