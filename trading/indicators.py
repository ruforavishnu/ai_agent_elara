import pandas as pd


class Indicators:

    @staticmethod
    def bollinger_bands(df: pd.DataFrame, period: int = 20, std_dev: float = 2):
        """
        Adds Bollinger Bands to DataFrame:
        - bb_middle (SMA)
        - bb_upper
        - bb_lower
        """

        df = df.copy()

        df["bb_middle"] = df["close"].rolling(window=period).mean()
        df["bb_std"] = df["close"].rolling(window=period).std()

        df["bb_upper"] = df["bb_middle"] + (std_dev * df["bb_std"])
        df["bb_lower"] = df["bb_middle"] - (std_dev * df["bb_std"])

        return df

    @staticmethod
    def awesome_oscillator(df: pd.DataFrame):
        """
        Awesome Oscillator (AO):
        AO = SMA(5, median price) - SMA(34, median price)
        """

        df = df.copy()

        # Median price
        df["median_price"] = (df["high"] + df["low"]) / 2

        # Short and long SMAs
        df["ao_short"] = df["median_price"].rolling(window=5).mean()
        df["ao_long"] = df["median_price"].rolling(window=34).mean()

        df["ao"] = df["ao_short"] - df["ao_long"]

        return df