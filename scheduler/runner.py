import time
from datetime import datetime



print("🤖 ETH Agent started")
print(f"🕒 System time: {datetime.utcnow()} UTC")


from market.eth_data import fetch_eth_candles
from trading.pipeline import run_pipeline
from trading.strategy import is_trading_time


def run_agent_loop(
    symbol: str = "ETHUSDT",
    timeframe: str = "15m",
    sleep_seconds: int = 900  # 15 minutes
):
    print("🤖 ETH Agent started")

    while True:
        now = datetime.now()

        if is_trading_time(now):
            print(f"\n⏰ {now.isoformat()} — Checking market")

            df = fetch_eth_candles(timeframe=timeframe)

            run_pipeline(
                symbol=symbol,
                high=df["high"].tolist(),
                low=df["low"].tolist(),
                close=df["close"].tolist(),
                account_balance=10_000,
                risk_percent=1.0,
                now=now
            )
        else:
            print(f"🌙 Outside trading hours: {now.time()}")

        time.sleep(sleep_seconds)



if __name__ == "__main__":
    run_agent_loop()
