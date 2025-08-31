
from abc import ABC, abstractmethod
from src.core.models.asset import Asset
from src.core.ports.broker_trade_port import BrokerTradePort
from src.core.ports.market_data_port import MarketDataPort
from src.core.models.bar import Bar

class Strategy(ABC):
    def __init__(self, broker: BrokerTradePort, asset: Asset):
        self.broker = broker
        self.asset = asset

    @abstractmethod
    def evaluate(self, bar_data:list[Bar]):
        raise NotImplementedError("Subclasses must implement the evaluate method.")
