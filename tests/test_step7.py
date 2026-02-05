import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from market.eth_data import fetch_eth_candles

df = fetch_eth_candles()

print(df.tail())

assert not df.empty
assert all(col in df.columns for col in ["open", "high", "low", "close"])

print("✅ Live ETH market data fetched")
