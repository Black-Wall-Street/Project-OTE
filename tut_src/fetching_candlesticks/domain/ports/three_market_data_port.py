from abc import ABC, abstractmethod
from datetime import datetime
from domain.models.two_bar import Bar
from domain.models.one_asset import Asset

class MarketDataPort(ABC):
    """
    Abstract Port defining how market data can be fetched and consumed.
    """

    @abstractmethod
    def request_historical_data(self, asset: Asset, start_date: datetime, end_date: datetime):
        """
        Pull historical data for a given asset within a time range.
        """
        pass

    @abstractmethod
    def next_bar(self, asset: Asset) -> Bar | None:
        """
        Return the next available bar for the given asset.
        """
        pass
