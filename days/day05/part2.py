def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]
    
def parse_range(from_to_range:str):
    range_list = from_to_range.split("-")
    assert int(range_list[0]) <= int(range_list[1])
    return (int(range_list[0]), int(range_list[1]) + 1)
    
def sort_by_starting_id_and_build_dict(ranges_list:list):
    """Sorts ranges by their start id"""
    ranges_dict = {}
    starter_list = []
    for item in ranges_list:
        rang_tuple = parse_range(item)
        if rang_tuple[0] not in ranges_dict:
            ranges_dict[rang_tuple[0]] = rang_tuple
            starter_list.append(rang_tuple[0])
        else:
            if ranges_dict[rang_tuple[0]][1] <= rang_tuple[1]:
                ranges_dict[rang_tuple[0]] = rang_tuple
    starter_list.sort()
    return starter_list, ranges_dict

# def combine_ranges(starter_list:list, ranges_dict:dict):
#     """Combine overlapping OR adjacent ranges."""
#     for i in range(len(starter_list)-1,0,-1):
#         member = starter_list[i]
#         next_member = starter_list[i-1]
#         next_member_from_to = ranges_dict[next_member]
#         if member <= next_member_from_to[1]:
#             new_end = max(next_member_from_to[1], ranges_dict[member][1])
#             ranges_dict[next_member] = (ranges_dict[next_member][0],new_end)
#             del ranges_dict[member]
#             starter_list[i] = -1
#     clean_starter_list = []
#     for item in starter_list:
#         if item != -1:
#             clean_starter_list.append(item)
#     return clean_starter_list, ranges_dict

def combine_ranges(starter_list: list, ranges_dict: dict):
    if not starter_list:
        return [], {}

    starts = sorted(starter_list)
    merged = []

    cur_start = starts[0]
    cur_end = ranges_dict[cur_start][1]  # end-exclusive

    for s in starts[1:]:
        a, b = ranges_dict[s]
        if a <= cur_end:          # use < for overlap-only, <= for overlap+adjacent
            cur_end = max(cur_end, b)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = a, b

    merged.append((cur_start, cur_end))

    new_starts = [a for a, _ in merged]
    new_dict = {a: (a, b) for a, b in merged}
    return new_starts, new_dict
            
    
def workup_ranges(ranges_list:list):
    start_list, rang_dict = sort_by_starting_id_and_build_dict(ranges_list)
    clean_start_list, ranges_dict = combine_ranges(start_list, rang_dict)
    return clean_start_list, ranges_dict
    
def solve(data):
    ranges_list = []
    ingredient_ids = []
    fresh_count = 0
    mode = "ranges"
    for line in data:
        if line:
            if mode == "ranges":
                ranges_list.append(line)
            else:
                ingredient_ids.append(int(line))    
        else:
            mode = "ingredients"
            continue
    
    clean_start_list, ranges_dict = workup_ranges(ranges_list)
    for start in clean_start_list:
        range_start, range_end_exclusive = ranges_dict[start]
        fresh_count += range_end_exclusive - range_start
    return fresh_count

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))