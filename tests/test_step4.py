import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from trading.risk import calculate_sl_tp, calculate_position_size

entry = 100
risk_price = 1
direction = "LONG"

sl, tp = calculate_sl_tp(entry, risk_price, direction)

print("Entry:", entry)
print("SL:", sl)
print("TP:", tp)
print("RR:", (tp - entry) / (entry - sl))

position = calculate_position_size(
    account_balance=1000,
    risk_percent=1,
    entry=entry,
    stop_loss=sl
)

print("Position size:", position)

if abs((tp - entry) / (entry - sl) - 2) < 0.01:
    print("✅ Risk–Reward enforced")
else:
    print("❌ Risk–Reward incorrect")
