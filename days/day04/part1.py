import numpy as np

def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]
    
def at_most_3_in_moore_neighborhood(arr:np.array):
    center = arr[1:-1, 1:-1]
    
    up = arr[0:-2, 1:-1]
    down = arr[2:, 1:-1]
    left = arr[1:-1, 0:-2]
    right = arr[1:-1, 2:]
    
    up_left = arr[0:-2, 0:-2]
    up_right = arr[0:-2, 2:]
    down_left = arr[2:, 0:-2]
    down_right =arr[2:, 2:]
    
    count = (
        (up == '@').astype(int) +
        (down == '@').astype(int) +
        (left == '@').astype(int) +
        (right == '@').astype(int) +
        (up_left == '@').astype(int) +
        (up_right == '@').astype(int) +
        (down_left == '@').astype(int) +
        (down_right == '@').astype(int)
    )
    return (center == '@') & (count <= 3)

def solve(data):
    arr = np.array([list(row) for row in data])
    arr_padded = np.pad(arr, pad_width=1, mode='constant', constant_values='.')
    mask = at_most_3_in_moore_neighborhood(arr_padded)
    total_true = np.count_nonzero(mask)
    return total_true

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
