from aocd import get_data
from pathlib import Path
from .utils import write_input, get_day_path

def ensure_input(day: int, year: int | None = None) -> str:
    day_path = get_day_path(day)
    day_path.mkdir(parents=True, exist_ok=True)
    input_file = day_path / "input.txt"

    if input_file.exists():
        return input_file.read_text()

    # Auto-download input
    text = get_data(day=day, year=year)
    write_input(input_file, text)
    return text
