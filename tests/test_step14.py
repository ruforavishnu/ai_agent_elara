from market.eth_data import ETHDataFetcher

try:
    fetcher = ETHDataFetcher()
    df = fetcher.fetch()

    print(df.tail())

    # Basic checks
    assert len(df) > 0
    assert "close" in df.columns

    print("✅ Step 9 market data fetch OK")

except Exception as e:
    print("❌ Step 9 test failed:", e)