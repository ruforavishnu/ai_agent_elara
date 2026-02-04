import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from trading.indicators import awesome_oscillator, bollinger_bands

# Mock OHLC data
data_len = 60
high = pd.Series(range(10, 10 + data_len))
low = pd.Series(range(5, 5 + data_len))
close = pd.Series(range(7, 7 + data_len))

ao = awesome_oscillator(high, low)
middle, upper, lower = bollinger_bands(close)

print("AO last value:", ao.iloc[-1])
print("BB middle last:", middle.iloc[-1])
print("BB upper last:", upper.iloc[-1])
print("BB lower last:", lower.iloc[-1])

if ao.isna().sum() < len(ao):
    print("✅ AO calculation OK")
else:
    print("❌ AO calculation FAILED")

if middle.isna().sum() < len(middle):
    print("✅ Bollinger Bands OK")
else:
    print("❌ Bollinger Bands FAILED")
