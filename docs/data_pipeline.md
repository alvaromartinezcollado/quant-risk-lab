# Data Pipeline

## Objective

The objective of this module is to collect, clean and prepare financial market data for quantitative risk and decision analysis.

## Data Source

The first version of the project uses historical daily data downloaded from Yahoo Finance through the `yfinance` Python package.

## Asset Universe

The initial asset universe includes:

- AAPL: Apple
- MSFT: Microsoft
- NVDA: NVIDIA
- JPM: JPMorgan Chase
- XOM: Exxon Mobil
- SPY: S&P 500 ETF
- TLT: US Treasury Bonds ETF
- GLD: Gold ETF

This selection combines technology, banking, energy, broad equity exposure, government bonds and gold.

## Data Field Used

The main field used for analysis is Adjusted Close.

Adjusted Close is used because it accounts for corporate actions such as stock splits and dividends.

## Cleaning Process

The cleaning process includes:

- sorting dates;
- removing duplicated dates;
- removing empty rows;
- forward-filling small missing gaps;
- dropping remaining missing values.

## Pipeline Outputs

The pipeline produces:

- raw market data;
- cleaned adjusted close prices;
- simple daily returns;
- logarithmic daily returns.

## Next Steps

The cleaned data will be used for:

- volatility analysis;
- correlation analysis;
- portfolio risk metrics;
- stress testing;
- Monte Carlo simulation;
- decision optimisation.