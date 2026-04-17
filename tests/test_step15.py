from market.eth_data import ETHDataFetcher
from trading.indicators import Indicators

try:
    fetcher = ETHDataFetcher()
    df = fetcher.fetch()

    # Apply indicators
    df = Indicators.bollinger_bands(df)
    df = Indicators.awesome_oscillator(df)

    print(df.tail())

    # Checks
    assert "bb_upper" in df.columns
    assert "bb_lower" in df.columns
    assert "ao" in df.columns

    print("✅ Step 10 indicators OK")

except Exception as e:
    print("❌ Step 10 test failed:", e)