import numpy as np


def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]
    
def solve(data):
    rows = [line.split() for line in data if line]
    arr = np.array(rows)
    m = arr.shape[1]
    
    arr_mult = arr.copy()
    mask = (arr_mult[-1] == "+") 
    arr_mult[:, mask] = "0"
    arr_mult = arr_mult[:-1]
    arr_mult = arr_mult.astype(int)
    prod_sum = np.sum(np.prod(arr_mult, axis=0))    
    
    arr_add = arr.copy()
    mask = (arr_add[-1] == "*") 
    arr_add[:, mask] = "0"
    arr_add = arr_add[:-1]
    arr_add = arr_add.astype(int)
    sum_sum = np.sum(np.sum(arr_add, axis=0))  
    
    return prod_sum + sum_sum

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
