import pytest
from days.day06.part1 import solve as solve1
from days.day06.part2 import solve as solve2

def test_day06_part1_example():
    test_data = [
        "123 328  51 64",
        "45 64  387 23",
        "6 98  215 314",
        "*   +   *   +",
    ]

    assert solve1(test_data) == 4277556
    
def test_day06_part2_example():
    test_data = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    assert solve2(test_data) == 3263827