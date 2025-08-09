from abc import ABC, abstractmethod
from src.core.models.bar import Bar
from src.core.models.asset import Asset
from datetime import datetime

class MarketDataPort(ABC):

    @abstractmethod
    def next_bar(self, asset: Asset) -> Bar:
        pass

    @abstractmethod
    def request_historical_data(self, asset: Asset, start_date: datetime, end_date: datetime):
        pass