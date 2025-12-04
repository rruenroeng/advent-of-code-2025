def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    current = 50
    count = 0
    for line in data:
        direction = line[0]
        magnitude = int(line[1:])
        was_zero_to_start = current == 0
        if direction == "L":
            current = current - magnitude % 100
        else:
            current = current + magnitude % 100
        if current < 0:
            current + 100
        # If current greater than 100 or less than 0 add 1 to count. (but not if it is 0 because that'd double-count)
        if not was_zero_to_start and (current > 100 or current < 0):
            count = count + 1
        current = current % 100
        if(current) == 0:
            count = count + 1
        # Add to count the number of times the sheer magnitude caused us to pass 0
        count = count + magnitude // 100
        
    return count

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))

# Two new edge cases to handle 