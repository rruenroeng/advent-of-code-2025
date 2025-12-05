def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):       
    return data[0]


if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))

# Two new edge cases to handle 