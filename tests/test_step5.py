import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from trading.execution import Order, execute_order

order = Order(
    symbol="ETHUSDT",
    direction="LONG",
    entry=100,
    stop_loss=99,
    take_profit=102,
    position_size=10,
    timestamp="TEST"
)

report = execute_order(order)

if report["status"] == "FILLED":
    print("✅ Order execution successful")
else:
    print("❌ Order execution failed")
