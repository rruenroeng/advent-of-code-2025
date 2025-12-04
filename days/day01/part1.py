def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    current = 50
    count = 0
    for line in data:
        direction = line[0]
        magnitude = int(line[1:])
        if direction == "L":
            current = current - magnitude % 100
        else:
            current = current + magnitude % 100
        if current < 0:
            current + 100
        current = current % 100
        if(current) == 0:
            count = count + 1
        
    return count

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
