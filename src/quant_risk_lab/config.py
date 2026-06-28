from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "JPM",
    "XOM",
    "SPY",
    "TLT",
    "GLD",
]

START_DATE = "2015-01-01"
END_DATE = None