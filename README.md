# DIM013 Project

A simple Python project demonstrating Git workflows, project organization, virtual environments, and CSV data loading with pandas.

## Project Structure

- `data/raw/` — Original CSV datasets.
- `data/processed/` — Processed datasets.
- `src/` — Python source code.
- `tests/` — Tests.
- `notebooks/` — Jupyter notebooks.
- `requirements.txt` — Python dependencies.

## Installation

Clone the repository:

```bash
git clone https://github.com/fbarbieri-max/dim013-project.git
cd dim013-project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the CSV loader:

```bash
python -m src.load_data data/raw/sample.csv
```

The program reads the CSV file using pandas and prints the first five rows.

## Git Workflow

This project demonstrates feature branches, Conventional Commits, merge conflict resolution, and GitHub collaboration.

## Contributing

Create a branch, make your changes, commit 
them, and open a Pull Request for review.

## Author

Francesco Barbieri
