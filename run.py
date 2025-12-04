import importlib
import sys
from src.utils import get_day_path
from src.aoc_client import ensure_input
from dotenv import load_dotenv
import os

load_dotenv()  # ensure environment is loaded

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <day> [part]")
        return

    day = int(sys.argv[1])
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    day_path = get_day_path(day)
    module_name = f"days.day{day:02d}.part{part}"

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found.")
        return

    # Ensure input exists (auto-download)
    input_text = ensure_input(day, year=os.getenv("AOC_YEAR", None))
    data = input_text.splitlines()

    answer = module.solve(data)
    print(f"Day {day} Part {part}: {answer}")

if __name__ == "__main__":
    main()
