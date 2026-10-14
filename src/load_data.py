import sys

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame.

    Args:
        path: Relative path to the CSV file.

    Returns:
        The loaded data.
    """
    return pd.read_csv(path, encoding="utf-8-sig", sep=",")


def count_rows(df: pd.DataFrame) -> int:
    """Count the rows of a DataFrame.

    Args:
        df: The DataFrame to count.

    Returns:
        The number of rows.
    """
    return len(df)


if __name__ == "__main__":
    print(load_data(sys.argv[1]).head())