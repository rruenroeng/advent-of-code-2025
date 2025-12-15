from collections import defaultdict
from typing import Dict


def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]
    
def solve(data:list[str]):
    start = data[0].index("S")
    flux: Dict[int, int] = {start: 1}
    length = len(data[0])
    totals: Dict[int, int] = defaultdict(int)
    hit = False
    for i in range(len(data)):
        new_flux = defaultdict(int)
        for j, count in flux.items():
            if data[i][j] == "^":
                # split: count goes left and right
                if j > 0:
                    new_flux[j - 1] += count
                    totals[j - 1] += count
                if j + 1 < length:
                    new_flux[j + 1] += count
                    totals[j + 1] += count
            else:
                # straight down
                new_flux[j] += count
                totals[j] += count
        # Create a string copy
        flux = new_flux        
    return sum(flux.values())

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
