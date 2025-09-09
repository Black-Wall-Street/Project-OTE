#Utils
from datetime import datetime, timedelta
from src.core.services.ibapi_client import IBApi

# Domain Objects
from src.core.models.asset import Asset, AssetType
from src.core.models.bar import Bar

# Indicators
from src.core.logic.indicators.crossings import GoldenCross, DeathCross

# Strategies
from core.logic.engines.trading_engine import TradingEngine
from core.logic.strategies.moving_average import MovingAverageCrossoverStrategy

# Adapters
from src.core.adapters.market_data.ib_market_adapter import IbApiDataAdapter
from src.core.adapters.broker_trade.ib_broker_adapter import IbBrokerAdapter


if __name__ == "__main__":
    asset = Asset(AssetType.FOREX, "EUR", "USD")
    ib_api = IBApi()
    market_data_adapter = IbApiDataAdapter(ib_api)
    market_data_adapter.request_historical_data(asset, datetime.today() - timedelta(days=300))
    broker_adapter = IbBrokerAdapter(ib_api)
    golden_cross = GoldenCross()
    death_cross = DeathCross()
    strategy = MovingAverageCrossoverStrategy(broker_adapter, asset, golden_cross, death_cross)
    trading_engine = TradingEngine(broker_adapter, market_data_adapter, [strategy], [golden_cross, death_cross])
    trading_engine.run(asset, threaded=True)
