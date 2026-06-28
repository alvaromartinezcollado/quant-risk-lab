import pandas as pd

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR


def load_raw_data(
    filename: str = "market_data_raw.csv",
) -> pd.DataFrame:
    """
    Load raw market data from CSV.
    """
    path = RAW_DATA_DIR / filename

    data = pd.read_csv(
        path,
        header=[0, 1],
        index_col=0,
        parse_dates=True,
    )

    return data


def extract_adjusted_close(data: pd.DataFrame) -> pd.DataFrame:
    """
    Extract adjusted close prices from Yahoo Finance data.
    """
    adjusted_close = data["Adj Close"]
    adjusted_close = adjusted_close.sort_index()

    return adjusted_close


def clean_prices(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Clean adjusted close prices.
    """
    prices = prices[~prices.index.duplicated(keep="first")]
    prices = prices.dropna(how="all")
    prices = prices.ffill()
    prices = prices.dropna()

    return prices


def save_processed_data(
    prices: pd.DataFrame,
    filename: str = "adjusted_close_prices.csv",
) -> None:
    """
    Save cleaned adjusted close prices.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DATA_DIR / filename
    prices.to_csv(output_path)

    print(f"Processed prices saved to: {output_path}")


def main() -> None:
    raw_data = load_raw_data()
    adjusted_close = extract_adjusted_close(raw_data)
    clean_data = clean_prices(adjusted_close)
    save_processed_data(clean_data)


if __name__ == "__main__":
    main()