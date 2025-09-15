from src.utils.logger import logger
from src.core.models.bar import Bar
from src.core.logic.indicators.indicator import Indicator


class RSI(Indicator):

    def __init__(self, period: int = 14):
        super().__init__()
        self.period = period
        self.data_rsi: list[float] = []

    def _compute_last_rsi(self, closes: list[float]) -> float | None:
        if len(closes) < self.period + 1:
            return None

        delta = [closes[i] - closes[i - 1] for i in range(1, len(closes))]

        gains = [d if d > 0 else 0.0 for d in delta[-self.period:]]
        losses = [-d if d < 0 else 0.0 for d in delta[-self.period:]]

        avg_gain = sum(gains) / self.period
        avg_loss = sum(losses) / self.period

        if avg_loss == 0:
            rs = float("inf") if avg_gain > 0 else 0.0
        else:
            rs = avg_gain / avg_loss

        rsi = 100.0 - (100.0 / (1.0 + rs))
        return rsi

    def compute(self, bar_data: list[Bar]) -> None:
        if len(bar_data) <= self.period:
            logger.debug(
                f"Insufficient ammount of data to compute {self.period}-bar RSI. "
                f"Only {len(bar_data)} bars available."
            )
            return

        closes = [bar.close for bar in bar_data]
        last_rsi = self._compute_last_rsi(closes)
        if last_rsi is None:
            logger.debug(
                f"Insufficient ammount of data to compute {self.period}-bar RSI. "
                f"Only {len(bar_data)} bars available."
            )
            return

        self.data_rsi.append(last_rsi)
        while len(self.data_rsi) > (self.period + 2):
            self.data_rsi.pop(0)

        self._state = False


class RSIOverbought(RSI):

    def __init__(self, period: int = 14, level: float = 70.0):
        super().__init__(period=period)
        self.level = level

    def compute(self, bar_data: list[Bar]) -> None:
        super().compute(bar_data)

        if len(self.data_rsi) < 1:
            return

        current_rsi = self.data_rsi[-1]
        prev_rsi = self.data_rsi[-2] if len(self.data_rsi) > 1 else None
        current_time = bar_data[-1].timestamp if bar_data else None

        self._state = current_rsi >= self.level

        if prev_rsi is not None and prev_rsi < self.level <= current_rsi:
            logger.info(
                f"RSI {self.period} crossed up into overbought (≥{self.level:.0f}) at {current_time} "
                f"(RSI={current_rsi:.2f})"
            )


class RSIOversold(RSI):

    def __init__(self, period: int = 14, level: float = 30.0):
        super().__init__(period=period)
        self.level = level

    def compute(self, bar_data: list[Bar]) -> None:
        super().compute(bar_data)

        if len(self.data_rsi) < 1:
            return

        current_rsi = self.data_rsi[-1]
        prev_rsi = self.data_rsi[-2] if len(self.data_rsi) > 1 else None
        current_time = bar_data[-1].timestamp if bar_data else None

        self._state = current_rsi <= self.level

        if prev_rsi is not None and prev_rsi > self.level >= current_rsi:
            logger.info(
                f"RSI {self.period} crossed down into oversold (≤{self.level:.0f}) at {current_time} "
                f"(RSI={current_rsi:.2f})"
            )
