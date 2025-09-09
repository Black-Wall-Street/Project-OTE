from src.core.logic.indicators.crossings import DeathCross, GoldenCross
from core.logic.engines.trading_engine import TradingEngine
from src.core.adapters.market_data.yf_market_adapter import YFMarketDataAdapter
from core.logic.strategies.moving_average import MovingAverageCrossoverStrategy
from src.core.adapters.broker_trade.custom_broker_adapter import CustomBrokerAdapter
from core.logic.engines.monte_carlo_permutator import MonteCarloPermutator
from src.core.adapters.result_plotter.plotly_plotter_adapter import PlotlyResultPlotterAdapter
from src.core.models.bar import Bar
from src.core.models.asset import Asset, AssetType
from datetime import datetime, timedelta

if __name__ == "__main__":
    asset = Asset(AssetType.FOREX, "EUR", "USD")
    market_data_adapter = YFMarketDataAdapter(asset)
    market_data_adapter.request_historical_data(asset, datetime.today()-timedelta(365*4), datetime.today())
    
    # Create the Monte Carlo Permutated objects
    permutator = MonteCarloPermutator(market_data_adapter, 1)
    broker_results: list[CustomBrokerAdapter] = []
    for market_adapter_iteration in permutator.permuted_adapters:
        broker_adapter = CustomBrokerAdapter(200, market_adapter_iteration)
        
        # Create indicator objects
        golden_cross = GoldenCross()
        death_cross = DeathCross()
        strategy = MovingAverageCrossoverStrategy(broker_adapter, asset, golden_cross, death_cross)

        trading_engine = TradingEngine(broker_adapter, market_adapter_iteration, [strategy], [golden_cross, death_cross])
        trading_engine.run(asset, threaded=False)
        PlotlyResultPlotterAdapter.plot(trading_engine.bar_data, trading_engine.portfolio_value, asset, asset.currency)
        broker_results.append(broker_adapter)


    pass