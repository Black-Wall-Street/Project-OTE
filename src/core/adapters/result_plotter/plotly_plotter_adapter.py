import plotly as py
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Type
from datetime import datetime

from src.utils.config import RISK_FREE_RATE
from src.core.models.bar import Bar
from src.core.ports.result_plotter_port import ResultPlotterPort


class PlotlyResultPlotterAdapter(ResultPlotterPort):

    @classmethod
    def plot(
        cls: Type["PlotlyResultPlotterAdapter"],
        bar_data: list[Bar],
        portfolio_value: dict[datetime, int],
        asset_name: str,
        currency: str,
    ) -> None:

        dates = [bar.timestamp for bar in bar_data]
        opens = [bar.open for bar in bar_data]
        highs = [bar.high for bar in bar_data]
        lows = [bar.low for bar in bar_data]
        closes = [bar.close for bar in bar_data]

        equity_dates = list(portfolio_value.keys())
        equity_values = list(portfolio_value.values())

        returns = cls._compute_daily_returns(equity_values)
        sharpe_ratio = cls._compute_sharpe_ratio(returns)
        drawdowns, max_drawdown = cls._compute_drawdown(equity_values)


        fig = make_subplots(
            rows=3, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=[f"{asset_name} Price", "Account Equity", "Drawdown (%)"]
        )

        # Candlestick chart
        fig.add_trace(go.Candlestick(
            x=dates,
            open=opens,
            high=highs,
            low=lows,
            close=closes,
            name="Asset Price"
        ), row=1, col=1)

        # Equity curve
        fig.add_trace(go.Scatter(
            x=equity_dates,
            y=equity_values,
            mode="lines",
            name="Account Equity",
            line=dict(color="cyan", width=2)
        ), row=2, col=1)

        # Drawdown curve (as percentage)
        fig.add_trace(go.Scatter(
            x=equity_dates,
            y=[dd * 100 for dd in drawdowns],  # percent
            mode="lines",
            name="Drawdown (%)",
            line=dict(color="red", width=1, dash="dot"),
            fill="tozeroy",
            fillcolor="rgba(255,0,0,0.5)",  
            yaxis="y3"
        ), row=3, col=1)

        fig.update_layout(
            title=f"Historical Data & Account Equity - {asset_name} | Sharpe Ratio: {sharpe_ratio:.4f}",
            xaxis_title="Date",
            template="plotly_dark",
            xaxis_rangeslider_visible=False,
            height=1200
        )
        fig.update_yaxes(title_text=f"{asset_name} Price ({currency})", row=1, col=1)
        fig.update_yaxes(title_text=f"Account Equity ({currency})", row=2, col=1)
        fig.update_yaxes(title_text=f"Drawdown (%)", row=3, col=1)

        py.offline.plot(fig)

    @classmethod
    def _compute_daily_returns(cls: Type["PlotlyResultPlotterAdapter"], equity_values: list[float]) -> list[float]:
        # Compute daily returns from equity curve manually
        returns = []
        for i in range(1, len(equity_values)):
            prev = equity_values[i - 1]
            curr = equity_values[i]
            if prev != 0:
                returns.append((curr - prev) / prev)
            else:
                returns.append(0.0)
        return returns
    
    @classmethod
    def _compute_mean(cls: Type["PlotlyResultPlotterAdapter"], returns: list[float]) -> float:
        return sum(returns) / len(returns) if returns else 0.0

    @classmethod
    def _compute_standard_deviation(cls: Type["PlotlyResultPlotterAdapter"], returns: list[float]) -> float:
        
        # Mean return
        mean_return = cls._compute_mean(returns)

        # Standard deviation
        std_return = 0.0
        if returns:
            mean = mean_return
            variance = sum((r - mean) ** 2 for r in returns) / len(returns)
            std_return = variance ** 0.5

        
        return std_return
    
    @classmethod
    def _compute_sharpe_ratio(cls: Type["PlotlyResultPlotterAdapter"], returns: list[float]) -> float:

        mean_return = cls._compute_mean(returns)
        std_return = cls._compute_standard_deviation(returns)

        sharpe_ratio = 0.0
        if std_return > 0:
            sharpe_ratio = (mean_return - RISK_FREE_RATE) / std_return

        return sharpe_ratio

    @classmethod
    def _compute_drawdown(cls, equity_values: list[float]) -> tuple[list[float], float]:
        if not equity_values:
            return [], 0.0
        
        peak = equity_values[0]
        drawdowns = []
        max_dd = 0.0

        for value in equity_values:
            if value > peak:
                peak = value
            dd = (value - peak) / peak
            drawdowns.append(dd)
            if dd < max_dd:
                max_dd = dd

        return drawdowns, max_dd
