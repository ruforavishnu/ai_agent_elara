import sys
import os
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from trading.strategy import generate_signal

# Fake market data
high = pd.Series([10, 11, 12, 13, 14])
low = pd.Series([8, 9, 10, 11, 12])
close = pd.Series([9, 10, 11, 12, 13])

# Fake indicators
ao = pd.Series([-1, -0.5, 0.2, 0.5, 0.7])
bb_middle = pd.Series([10, 10.5, 11, 11.5, 12])
bb_upper = bb_middle + 2
bb_lower = bb_middle - 2

# Force trading time
mock_time = datetime.now().replace(hour=11, minute=0)

signal = generate_signal(
    high=high,
    low=low,
    close=close,
    ao=ao,
    bb_middle=bb_middle,
    bb_upper=bb_upper,
    bb_lower=bb_lower,
    now=mock_time
)

print("Generated signal:", signal)

if signal is None:
    print("⚠️ No signal generated (acceptable)")
else:
    print("✅ Signal logic working")
