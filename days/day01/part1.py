# part1.py

def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    # TODO: write puzzle logic here
    return None

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
