import ccxt
import pandas as pd


def fetch_eth_candles(
    timeframe: str = "15m",
    limit: int = 100
):
    exchange = ccxt.binance()

    ohlcv = exchange.fetch_ohlcv(
        symbol="ETH/USDT",
        timeframe=timeframe,
        limit=limit
    )

    df = pd.DataFrame(
        ohlcv,
        columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    return df
