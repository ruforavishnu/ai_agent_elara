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



def calculate_trade(
    account_balance: float,
    risk_percent: float,
    entry: float,
    direction: str
) -> TradeRisk:
    """
    High-level trade risk calculator
    Enforces 1:2 RR always
    """

    # 1. Decide absolute risk per trade (price movement)
    risk_amount_price = entry * (risk_percent / 100)

    # 2. Calculate SL and TP
    stop_loss, take_profit = calculate_sl_tp(
        entry=entry,
        risk_amount=risk_amount_price,
        direction=direction
    )

    # 3. Calculate position size
    position_size = calculate_position_size(
        account_balance=account_balance,
        risk_percent=risk_percent,
        entry=entry,
        stop_loss=stop_loss
    )

    return TradeRisk(
        entry=entry,
        stop_loss=stop_loss,
        take_profit=take_profit,
        position_size=position_size
    )
