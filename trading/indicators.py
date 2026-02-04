import pandas as pd
import numpy as np



def awesome_oscillator(high: pd.Series, low: pd.Series) -> pd.Series:
    """
    Calculates Awesome Oscillator (AO)
    """
    median_price = (high + low) / 2
    sma_fast = median_price.rolling(window=5).mean()
    sma_slow = median_price.rolling(window=34).mean()
    ao = sma_fast - sma_slow
    return ao


def bollinger_bands(close: pd.Series, window: int = 20, num_std: int = 2):
    """
    Calculates Bollinger Bands
    Returns: middle, upper, lower
    """
    middle = close.rolling(window=window).mean()
    std = close.rolling(window=window).std()

    upper = middle + (std * num_std)
    lower = middle - (std * num_std)

    return middle, upper, lower
