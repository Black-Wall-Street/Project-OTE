from abc import ABC, abstractmethod
from src.core.models.bar import Bar
from src.utils.logger import logger

class Indicator(ABC):
    def __init__(self):
        self._state: bool = None

    @abstractmethod
    def compute(self, bar_data:list[Bar]) -> None:
        raise NotImplementedError("Subclasses must implement the evaluate method.")
    
    @property
    def state(self) -> bool:
        return self._state