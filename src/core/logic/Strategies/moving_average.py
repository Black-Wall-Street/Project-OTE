from src.core.logic.indicators.crossings import GoldenCross, DeathCross
from core.logic.strategies.strategy import Strategy
from src.core.models.asset import Asset, AssetType
from src.core.models.bar import Bar
from src.core.ports.broker_trade_port import BrokerTradePort
from src.utils.logger import logger


class MovingAverageCrossoverStrategy(Strategy):

    def __init__(self, broker, asset, golden_cross: GoldenCross, death_cross: DeathCross):
        super().__init__(broker, asset)
        self.golden_cross = golden_cross
        self.death_cross = death_cross

    def evaluate(self, bar_data: list[Bar]):

        current_price: float = bar_data[-1].low

        if (self.death_cross.state == True):
            self.broker.sell(self.asset, 1, current_price)

        elif (self.golden_cross.state == True):
            self.broker.buy(self.asset, 1, current_price)