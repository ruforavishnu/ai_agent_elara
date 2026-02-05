from dataclasses import dataclass


@dataclass
class TradeRisk:
    entry: float
    stop_loss: float
    take_profit: float
    position_size: float



def calculate_sl_tp(entry: float, risk_amount: float, direction: str) -> tuple[float, float]:
    """
    risk_amount: absolute price movement willing to lose
    """
    if direction not in ("LONG", "SHORT"):
        raise ValueError("Direction must be LONG or SHORT")

    if direction == "LONG":
        stop_loss = entry - risk_amount
        take_profit = entry + (risk_amount * 2)
    else:
        stop_loss = entry + risk_amount
        take_profit = entry - (risk_amount * 2)

    return stop_loss, take_profit





def calculate_position_size(
    account_balance: float,
    risk_percent: float,
    entry: float,
    stop_loss: float
) -> float:
    """
    risk_percent: e.g. 1 means 1% of account
    """
    risk_amount = account_balance * (risk_percent / 100)
    per_unit_risk = abs(entry - stop_loss)

    if per_unit_risk == 0:
        raise ValueError("Invalid SL: zero risk")

    position_size = risk_amount / per_unit_risk
    return round(position_size, 4)
