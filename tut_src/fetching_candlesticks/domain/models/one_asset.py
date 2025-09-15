from enum import Enum
from dataclasses import dataclass

class AssetType(Enum):
    FOREX = "forex"
    STOCK = "stock"

@dataclass(frozen=True)
class Asset:
    asset_type: AssetType
    symbol: str       
    currency: str     
