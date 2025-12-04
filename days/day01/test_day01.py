from days.day01.part1 import solve as solve1
from days.day01.part2 import solve as solve2

def test_day01_part1_example():
    test_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    assert solve1(test_data) == 3
    
def test_day01_part1_example():
    test_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    assert solve2(test_data) == 6
