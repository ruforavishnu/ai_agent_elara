



import requests
import pandas as pd


class ETHDataFetcher:
    BASE_URL = "https://api.binance.com/api/v3/klines"

    def __init__(self, symbol="ETHUSDT", interval="15m", limit=100):
        self.symbol = symbol
        self.interval = interval
        self.limit = limit

    def fetch(self) -> pd.DataFrame:
        params = {
            "symbol": self.symbol,
            "interval": self.interval,
            "limit": self.limit
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        df = pd.DataFrame(data, columns=[
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "qav", "num_trades",
            "taker_base_vol", "taker_quote_vol", "ignore"
        ])

        # Convert numeric columns
        for col in ["open", "high", "low", "close", "volume"]:
            df[col] = df[col].astype(float)

        # Convert timestamp
        df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

        return df[["open_time", "open", "high", "low", "close", "volume"]]