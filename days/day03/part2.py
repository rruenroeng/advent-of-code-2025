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
        prev_max_ind = -1
        digits_list = []
        for digits_from_end in range(12,0,-1):
            max_val, max_ind = find_greatest(line, prev_max_ind+1, len(line)-digits_from_end+2)
            prev_max_ind = max_ind
            digits_list.append(max_val)
            # total_joltage = total_joltage + int(str(max_left_val)+str(max_right_val))
        result = "".join(str(d) for d in digits_list)
        total_joltage = total_joltage + int(result)
    return total_joltage

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))

# Two new edge cases to handle 