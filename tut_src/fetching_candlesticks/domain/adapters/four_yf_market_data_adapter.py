from domain.ports.three_market_data_port import MarketDataPort
from domain.models.one_asset import Asset, AssetType
from domain.models.two_bar import Bar

import yfinance as yf
import tempfile
from datetime import datetime
from typing import List

class YFMarketDataAdapter(MarketDataPort):
    def __init__(self, asset: Asset):
        self.asset = asset
        self._bars: List[Bar] = []
        self._cursor: int = 0

    def request_historical_data(self, asset: Asset, start_date: datetime, end_date: datetime):
        print("Fetching data from yfinance...")

        if asset.asset_type != AssetType.FOREX:
            raise NotImplementedError("Only FOREX assets are supported for now.")

        yf_symbol = asset.symbol + "=X"  # e.g., "EURUSD=X"
        data = yf.download(yf_symbol, start=start_date, end=end_date)

        if data.empty:
            raise ValueError("No data returned from yfinance.")

        self._bars = [
            Bar(
                timestamp=index.to_pydatetime(),
                open=float(row["Open"]),
                high=float(row["High"]),
                low=float(row["Low"]),
                close=float(row["Close"]),
                volume=float(row["Volume"]),
            )
            for index, row in data.iterrows()
        ]

        print(f"Loaded {len(self._bars)} bars.")

    def next_bar(self, asset: Asset) -> Bar | None:
        if self._cursor < len(self._bars):
            bar = self._bars[self._cursor]
            self._cursor += 1
            return bar
        return None
