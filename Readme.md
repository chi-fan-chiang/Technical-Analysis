
# Bitcoin Technical Analysis Tool

This project uses Python along with the yfinance package to download Bitcoin (BTC-USD) historical and real-time data. It then applies technical indicators using the ta library.

## Features

- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Ichimoku Cloud
- Bollinger Bands

## Project Structure

```
.
├── btc_technical_analysis.py       # Downloads daily data from 2024-01-01 with technical indicators
├── 1min.py                        # Downloads 1-minute interval data for the past 7 days
└── README.md                      # Project documentation
```

## Quick Start

### Install dependencies

It is recommended to use a virtual environment. Install the required packages:

```bash
pip install yfinance ta pandas
```

### Daily data analysis

Run the script to download daily Bitcoin data starting from January 1, 2024:

```bash
python "btc_technical_analysis.py "
```

Output file: `btc_technical_analysis.csv`

### 1-minute data analysis

Run the script to get recent 1-minute interval data (up to 7 days):

```bash
python 1min.py
```

Output file: `btc_1min_technical_analysis.csv`

Note: Ichimoku indicators may contain many NaN values due to the need for longer time series.

## Technical Indicator Overview

- RSI: Detects overbought or oversold conditions.
- MACD: Identifies trend changes and strength.
- Ichimoku: Indicates support/resistance and trend direction.
- Bollinger Bands: Measures price volatility.

## Output

The script exports results with technical indicators to `.csv` format, ready for analysis or Excel import.

## Notes

- Yahoo Finance 1-minute data is limited to about 7 days.
- If download fails, check your network connection or API rate limits.

## Author

Developed by a Python and FinTech enthusiast. Feel free to open an issue for questions or suggestions.