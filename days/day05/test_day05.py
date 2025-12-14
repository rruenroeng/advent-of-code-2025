import pytest
from days.day05.part1 import solve as solve1
from days.day05.part2 import combine_ranges, solve as solve2, sort_by_starting_id_and_build_dict, workup_ranges

def test_day05_part1_example():
    test_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32"
    ]

    assert solve1(test_data) == 3
    
def test_day05_part2_example():
    test_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32"
    ]

    assert solve2(test_data) == 14
    
def test_overlapping_ranges_are_combined():
    # 1-3 => [1,4), 3-5 => [3,6) overlap at 3
    starter, d = sort_by_starting_id_and_build_dict(["1-3", "3-5"])
    starter, d = combine_ranges(starter, d)

    assert starter == [1]
    assert d[1] == (1, 6)  # [1,6) == 1..5 inclusive


def test_adjacent_ranges_are_combined():
    # Adjacent: 1-3 => [1,4), 4-6 => [4,7) touch at 4
    starter, d = sort_by_starting_id_and_build_dict(["1-3", "4-6"])
    starter, d = combine_ranges(starter, d)

    # Spec says these SHOULD combine
    assert starter == [1]
    assert d[1] == (1, 7)


def test_chain_of_adjacent_ranges_collapses_to_one():
    starter, d = sort_by_starting_id_and_build_dict(["1-2", "3-4", "5-5"])
    starter, d = combine_ranges(starter, d)

    assert starter == [1]
    assert d[1] == (1, 6)  # [1,6) == 1..5 inclusive


def test_contained_range_is_absorbed():
    # 1-10 fully covers 3-5
    starter, d = sort_by_starting_id_and_build_dict(["1-10", "3-5"])
    starter, d = combine_ranges(starter, d)

    assert starter == [1]
    assert d[1] == (1, 11)


def test_duplicate_start_keeps_widest_range():
    starter, d = sort_by_starting_id_and_build_dict(["1-3", "1-10", "12-12"])
    assert starter == [1, 12]
    assert d[1] == (1, 11)
    assert d[12] == (12, 13)


@pytest.mark.parametrize(
    "ranges, expected",
    [
        (["5-5"], ([5], {5: (5, 6)})),
        (["2-4", "10-10"], ([2, 10], {2: (2, 5), 10: (10, 11)})),
        (["10-12", "1-2", "3-9"], ([1], {1: (1, 13)})),  # becomes one big range
    ],
)
def test_workup_ranges_smoke(ranges, expected):
    clean_starters, d = workup_ranges(ranges)
    exp_starters, exp_d = expected
    assert clean_starters == exp_starters
    assert d == exp_d

# 359913027576323