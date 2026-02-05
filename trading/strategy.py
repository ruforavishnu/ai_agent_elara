from datetime import datetime, time
import pandas as pd


TRADING_START = time(10, 0)
TRADING_END = time(20, 0)


def is_trading_time(now: datetime | None = None) -> bool:
    if now is None:
        now = datetime.now()

    current_time = now.time()
    return TRADING_START <= current_time <= TRADING_END


def create_signal(direction: str, reason: str) -> dict:
    return {
        "direction": direction,  # "LONG" or "SHORT"
        "reason": reason,
        "timestamp": datetime.now().isoformat()
    }


def generate_signal(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    ao: pd.Series,
    bb_middle: pd.Series,
    bb_upper: pd.Series,
    bb_lower: pd.Series,
    now: datetime | None = None
):
    # Enforce trading window
    if not is_trading_time(now):
        return None

    # Use latest values
    ao_now = ao.iloc[-1]
    ao_prev = ao.iloc[-2]
    price = close.iloc[-1]

    # LONG condition:
    # AO crosses above zero AND price near lower Bollinger Band
    if ao_prev < 0 and ao_now > 0 and price <= bb_lower.iloc[-1]:
        return create_signal(
            direction="LONG",
            reason="AO bullish cross + price near lower BB"
        )

    # SHORT condition:
    # AO crosses below zero AND price near upper Bollinger Band
    if ao_prev > 0 and ao_now < 0 and price >= bb_upper.iloc[-1]:
        return create_signal(
            direction="SHORT",
            reason="AO bearish cross + price near upper BB"
        )

    return None
