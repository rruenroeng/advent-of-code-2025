import numpy as np


def read_input(path="input.txt"):
    with open(path) as f:
        return [line.split('\n') for line in f]

def column_product_from_strings(col: np.ndarray, mult_mode:bool) -> int:
    col = np.asarray(col, dtype=str)  # shape (n,)
    if col.size == 0:
        return 0

    # # 1) pad each string in the column to the max length with trailing zeros
    max_len = np.char.str_len(col).max()
    # padded = np.char.rjust(col, max_len, "0")  # right-pad with '0'

    # 2) make (n, max_len) character matrix
    chars = np.array([list(s) for s in col], dtype="U1")

    # 3) for each character position, concatenate down the rows -> int
    nums = [
        int(s) if (s := "".join(chars[:, j]).replace("0", "")) else 0
        for j in range(max_len)
    ]
    # 4) product of those numbers
    if mult_mode:
        total = 1
        for x in nums:
            total *= x
    else:
        total = 0
        for x in nums:
            total += x
    return total

def total_score(arr: np.ndarray, mult_mode:bool) -> int:
    arr = np.asarray(arr, dtype=str)  # shape (n, m)
    return sum(column_product_from_strings(arr[:, j], mult_mode) for j in range(arr.shape[1]))

def solve(data):
    rows = data[:-1]        # ignore last row (symbols)
    rows_chars = [list(r) for r in rows]

    for i in range(len(rows[0])):  # same length guaranteed
        # if every (non-last) row has a space here, leave as-is
        if all(r[i] == " " for r in rows):
            continue

        # otherwise, convert spaces to '0' in the (non-last) rows
        for rc in rows_chars:
            if rc[i] == " ":
                rc[i] = "0"

    # rebuild result (mask unchanged)
    new_data = ["".join(rc) for rc in rows_chars] + [data[-1]]
    rows = [line.split() for line in new_data if line]
    arr = np.array(rows)
    m = arr.shape[1]
    
    arr_mult = arr.copy()
    mask = (arr_mult[-1] == "+") 
    arr_mult[:, mask] = "0"
    arr_mult = arr_mult[:-1]
    prod_sum = total_score(arr_mult,True)
    
    arr_add = arr.copy()
    mask = (arr_add[-1] == "*") 
    arr_add[:, mask] = "0"
    arr_add = arr_add[:-1]
    sum_sum = total_score(arr_add,False)
    
    return prod_sum + sum_sum

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))