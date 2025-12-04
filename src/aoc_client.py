# src/aoc_client.py
from aocd import get_data
from pathlib import Path
from .utils import get_day_path, write_input

def ensure_input(day: int, year: int | None = None) -> str:
    day_path = get_day_path(day)
    day_path.mkdir(parents=True, exist_ok=True)

    input_file = day_path / "input.txt"

    # If already downloaded → load it
    if input_file.exists():
        return input_file.read_text()

    # Download from Advent of Code
    text = get_data(day=day, year=year)

    # Write to file
    write_input(input_file, text)

    return text
