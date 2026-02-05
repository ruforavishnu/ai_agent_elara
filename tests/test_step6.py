import sys
import os
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from trading.pipeline import run_pipeline

# Dummy market data (enough points for indicators)
high = list(range(102, 202))
low = list(range(100, 200))
close = list(range(100, 200))

# Force valid trading time (11:00 AM)
fake_now = datetime.now().replace(hour=11, minute=0, second=0)

report = run_pipeline(
    symbol="ETHUSDT",
    high=high,
    low=low,
    close=close,
    account_balance=10_000,
    risk_percent=1.0,
    now=fake_now
)

if report:
    print("✅ Full pipeline executed")
else:
    print("⚠️ Pipeline ended with no trade")
