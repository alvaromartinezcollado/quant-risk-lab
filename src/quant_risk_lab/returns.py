import numpy as np
import pandas as pd

from config import PROCESSED_DATA_DIR


def load_prices(
    filename: str = "adjusted_close_prices.csv",
) -> pd.DataFrame:
    """
    Load cleaned adjusted close prices.
    """
    path = PROCESSED_DATA_DIR / filename

    prices = pd.read_csv(
        path,
        index_col=0,
        parse_dates=True,
    )

    return prices


def compute_simple_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute simple daily returns.
    """
    returns = prices.pct_change()
    returns = returns.dropna()

    return returns


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute logarithmic daily returns.
    """
    returns = np.log(prices / prices.shift(1))
    returns = returns.dropna()

    return returns


def save_returns(
    returns: pd.DataFrame,
    filename: str,
) -> None:
    """
    Save returns to CSV.
    """
    output_path = PROCESSED_DATA_DIR / filename
    returns.to_csv(output_path)

    print(f"Returns saved to: {output_path}")


def main() -> None:
    prices = load_prices()

    simple_returns = compute_simple_returns(prices)
    log_returns = compute_log_returns(prices)

    save_returns(simple_returns, "simple_returns.csv")
    save_returns(log_returns, "log_returns.csv")


if __name__ == "__main__":
    main()