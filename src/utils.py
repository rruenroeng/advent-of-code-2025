import os
from pathlib import Path
from dotenv import load_dotenv

# Auto-load .env when utils is imported
load_dotenv()

def read_input(path: str) -> list[str]:
    with open(path) as f:
        return [line.rstrip("\n") for line in f]

def write_input(path: str, text: str):
    Path(path).write_text(text)

def get_day_path(day: int) -> Path:
    return Path("days") / f"day{day:02d}"
