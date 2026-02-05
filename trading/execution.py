from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    symbol: str
    direction: str
    entry: float
    stop_loss: float
    take_profit: float
    position_size: float
    timestamp: str




def validate_order(order: Order) -> None:
    if order.entry <= 0:
        raise ValueError("Invalid entry price")

    if order.position_size <= 0:
        raise ValueError("Invalid position size")

    if order.direction == "LONG":
        if not (order.stop_loss < order.entry < order.take_profit):
            raise ValueError("Invalid LONG SL/TP placement")
    elif order.direction == "SHORT":
        if not (order.take_profit < order.entry < order.stop_loss):
            raise ValueError("Invalid SHORT SL/TP placement")
    else:
        raise ValueError("Direction must be LONG or SHORT")



def execute_order(order: Order) -> dict:
    validate_order(order)

    execution_report = {
        "status": "FILLED",
        "symbol": order.symbol,
        "direction": order.direction,
        "entry": order.entry,
        "stop_loss": order.stop_loss,
        "take_profit": order.take_profit,
        "position_size": order.position_size,
        "executed_at": datetime.utcnow().isoformat()
    }

    print("🟢 ORDER EXECUTED (MOCK)")
    for k, v in execution_report.items():
        print(f"{k}: {v}")

    return execution_report


