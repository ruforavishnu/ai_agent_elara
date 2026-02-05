import pandas as pd
from datetime import datetime

from trading.strategy import generate_signal
from trading.risk import calculate_trade
from trading.execution import Order, execute_order
from trading.indicators import awesome_oscillator, bollinger_bands


def run_pipeline(
    symbol: str,
    high: list[float],
    low: list[float],
    close: list[float],
    account_balance: float,
    risk_percent: float = 1.0,
    now: datetime | None = None
):
    # 1. Convert to pandas Series
    high_s = pd.Series(high)
    low_s = pd.Series(low)
    close_s = pd.Series(close)

    # 2. Compute indicators
    ao = awesome_oscillator(high_s, low_s)
    bb_middle, bb_upper, bb_lower = bollinger_bands(close_s)

    # 3. Generate strategy signal
    signal = generate_signal(
        high=high_s,
        low=low_s,
        close=close_s,
        ao=ao,
        bb_middle=bb_middle,
        bb_upper=bb_upper,
        bb_lower=bb_lower,
        now=now
    )

    if signal is None:
        print("⚠️ No trade signal — pipeline stopped")
        return None

    # 4. Entry price = latest close
    entry_price = close_s.iloc[-1]

    # 5. Risk calculation (1:2 RR enforced internally)
    trade = calculate_trade(
        account_balance=account_balance,
        risk_percent=risk_percent,
        entry=entry_price,
        direction=signal["direction"]
    )

    # 6. Create order
    order = Order(
        symbol=symbol,
        direction=signal["direction"],
        entry=trade.entry,
        stop_loss=trade.stop_loss,
        take_profit=trade.take_profit,
        position_size=trade.position_size,
        timestamp=signal["timestamp"]
    )

    # 7. Execute (mock)
    return execute_order(order)
