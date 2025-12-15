def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]
    
def solve(data:list[str]):
    # Create a string copy
    mask = data[0][:].replace("S","|")
    length = len(mask)
    hit = False
    total = 0
    for i in range(len(data)):
        ind_where_new_pipes = []
        for j in range(len(mask)):
            if mask[j] == "|" and data[i][j] == "^":
                hit = True
                total = total + 1
                # Somewhere in the middle
                # if j > 0 and j < length - 1:
                #     data[i] = data[i].replace(".^.","|^|")
                # Beginning of the string
                if j < length - 1:
                    # data[i] = data[i].replace("^.","^|")
                    ind_where_new_pipes.append(j+1)
                # End of the string
                if j > 0:
                    # data[i] = data[i].replace(".^","|^")
                    ind_where_new_pipes.append(j-1)
            if i > 0 and data[i][j] != "^" and data[i-1][j] == "|":
                ind_where_new_pipes.append(j)
        # Create a string copy
        if not hit:
            data[i] = mask
        else:
            new_char_list = []
            for c in data[i]:
                new_char_list.append(c)
            for ind in ind_where_new_pipes:
                new_char_list[ind] = "|"
            data[i] = "".join(new_char_list)
        hit = False
        mask = data[i].replace("^",".")
        
    return total

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
