import pandas as pd
import yfinance as yf

from config import (
    TICKERS,
    START_DATE,
    END_DATE,
    RAW_DATA_DIR,
)

def download_market_data(
    tickers: list[str] = TICKERS,
    start: str = START_DATE,
    end: str | None = END_DATE,
) -> pd.DataFrame:
    """
    Download historical market data from Yahoo Finance.
    """
    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        auto_adjust=False,
        progress=True,
    )

    return data


def save_raw_data(
    data: pd.DataFrame,
    filename: str = "market_data_raw.csv",
) -> None:
    """
    Save raw market data to CSV.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_path = RAW_DATA_DIR / filename
    data.to_csv(output_path)

    print(f"Raw data saved to: {output_path}")


def main() -> None:
    data = download_market_data()
    save_raw_data(data)


if __name__ == "__main__":
    main()