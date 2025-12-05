Below is a clean, polished **README.md** for your repository.
It explains:

* How the project is structured
* How `run.py` works
* Where `aoc_client` and `utils` live
* How to create new day directories
* How to write solutions
* How inputs are automatically downloaded
* How to configure environment variables

All details are taken from your actual source files (and cited).

---

# 📘 Advent of Code — Python Runner

This repository provides a lightweight framework for solving **Advent of Code** puzzles.
It includes automatic input downloading, a simple day/part module structure, and a convenient CLI for running any solution.

---

## 🚀 Running a Solution

To run **day 1 part 1**, do:

```bash
python run.py 1 1
```

To run **day 5 part 2**:

```bash
python run.py 5 2
```

If part is omitted, it defaults to `1`:

```bash
python run.py 3
```

The runner uses:

* `src/aoc_client.ensure_input()` to download or load your input file 
* `src/utils.get_day_path()` to find the correct day directory 
* Dynamically imports your solution module:

  ```
  days/dayXX/partY.py
  ```

Example from `run.py`:
`module_name = f"days.day{day:02d}.part{part}"` 

---

## 📁 Project Structure

```
.
├── run.py                    # CLI entry point
├── days/
│   ├── day01/
│   │   ├── part1.py
│   │   └── input.txt
│   ├── day02/
│   │   └── part1.py
│   ...
├── src/
│   ├── aoc_client.py         # input downloader
│   ├── utils.py              # helpers (paths, read/write, env)
│   └── ...
├── requirements.txt
├── pytest.ini
└── .env.example
```

### `src/aoc_client.py`

Responsible for ensuring your puzzle input exists.
If `input.txt` is missing, it uses `advent-of-code-data`’s `get_data()` to fetch it automatically.


### `src/utils.py`

Provides:

* `read_input(path)`
* `write_input(path, text)`
* `get_day_path(day)` → `days/dayXX`
* Auto-loads `.env`


---

## 📝 Creating a New Day

Each day lives in:

```
days/dayXX/
```

For example:

```bash
mkdir -p days/day05
```

Inside, create `part1.py` (and optionally `part2.py`):

### Template for `part1.py`

```python
def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    pass

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
```

This matches how your previous days are structured.

When you run `python run.py 5 1`, your `solve()` receives a list of input lines from AoC, supplied via:

```python
data = input_text.splitlines()  # in run.py
```



---

## 📥 Automatic Input Download

`run.py` calls:

```python
input_text = ensure_input(day, year=os.getenv("AOC_YEAR", None))
```



`ensure_input()`:

1. Creates the directory `days/dayXX` if needed
2. If `input.txt` exists → read it
3. Otherwise → download via `get_data()`
4. Save it using `write_input()`

This logic is in `src/aoc_client.py` 

---

## 🔧 Environment Variables

You must provide:

* `AOC_SESSION` — your Advent of Code session cookie
* `AOC_YEAR` (optional) — defaults to current year

Use the provided `.env.example` as a template.

The `.env` file is loaded automatically because `src/utils.py` executes `load_dotenv()` on import.


Example `.env`:

```
AOC_SESSION=your_session_cookie_here
AOC_YEAR=2025
```

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

Dependencies (from `requirements.txt`):

* `python-dotenv`
* `advent-of-code-data`
* `rich`


---

## 🧪 Running Tests

`pytest.ini` sets the Python path so tests can import from `src/`.


Run tests:

```bash
pytest
```

---

## 🎄 Summary

This repo gives you:

* A structured folder layout for Advent of Code
* Automatic creation of `days/dayXX/`
* Automatic input downloading
* A clean function-per-part workflow
* A simple runner: `python run.py <day> <part>`
