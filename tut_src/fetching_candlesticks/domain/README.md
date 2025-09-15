# Fetching Candlesticks in Hexagonal Architecture

This tutorial demonstrates how to **fetch market candlestick data** (OHLCV) using the `yfinance` package within a **Hexagonal (Port-Adapter) Architecture**. The purpose is to teach the core idea of inbound/outbound ports by isolating market data access behind clean abstractions.

---

## 🌐 Project Context

This module is a **self-contained tutorial** separate from our trading logic. We use `YFMarketDataAdapter` to connect to Yahoo Finance while enforcing the hexagonal design.

Directory: `tut_src/fetching_candlesticks/`

---

## 📂 Directory Structure

```
fetching_candlesticks/
├── domain/
│   ├── models/
│   │   ├── one_asset.py
│   │   └── two_bar.py
│   ├── ports/
│   │   └── three_market_data_port.py
│   ├── adapters/
│   │   └── four_yf_market_data_adapter.py
│   ├── logic/
│       ├── five_fetch_bars.py
```

---

## 📝 Scripts Explained

### 1. `one_asset.py`

Defines `Asset` and `AssetType` as a `dataclass` and `Enum`, respectively.
This encapsulates a tradable symbol and its metadata.

### 2. `two_bar.py`

Defines the `Bar` class as a dataclass. This represents a single candlestick with OHLCV data and a timestamp.

### 3. `three_market_data_port.py`

Abstract base class (ABC) describing the interface that all Market Data Adapters must implement.

```python
class MarketDataPort(ABC):
    @abstractmethod
    def next_bar(...): pass

    @abstractmethod
    def request_historical_data(...): pass
```

### 4. `four_yf_market_data_adapter.py`

Concrete implementation of `MarketDataPort` using `yfinance`.

- Symbol formatting (e.g., `EURUSD` ➞ `EURUSD=X`)
- Uses `.download()` from yfinance to fetch historical data
- Transforms raw DataFrame into a list of `Bar` objects internally stored as `_list_data`
- Supports `.next_bar()` iteration

### 5. `five_fetch_bars.py`

**Walkthrough script** to:

- Instantiate an `Asset`
- Instantiate the `YFMarketDataAdapter`
- Request historical data between two dates
- Print the first few candlestick bars via `.next_bar()`

This script shows **the data journey** from inbound port through the adapter into the hexagon.

---

## ⚙️ How to Run

From the `tut_src/` directory, run:

```bash
python -m fetching_candlesticks.domain.logic.five_fetch_bars
```

Expected output:

```
Asset defined: EUR/USD (FOREX)
Adapter created: YFMarketDataAdapter
Fetching data from yfinance...
Bar 0: Time: 2024-09-01 00:00:00 | O: 1.0841 | H: 1.0862 | L: 1.0833 | C: 1.0857 | V: 83640200.0
Bar 1: Time: 2024-09-02 00:00:00 | O: 1.0857 | ...
```

---

## ⚠️ Common Errors

### 1. **Wrong Symbol Format**

```bash
['EURUSDUSD=X']: YFTzMissingError('possibly delisted; no timezone found')
```

**Fix**: Don't concatenate currency twice in the adapter.

```python
yf_symbol = asset.symbol + "=X"
```

### 2. **Empty `_list_data`**

Make sure:

- You actually called `.request_historical_data(...)`
- Your start and end dates are valid and include market days

### 3. **Direct access of private field**

```python
print(adapter._list_data)  # Not recommended
```

Access the data through `.next_bar()` method instead.

---

## 🧱 Purpose of the Walkthrough Script

This is your **observable data flow tool**. It shows:

- What data looks like inside the hexagon
- How ports and adapters isolate dependencies
- How data can be fetched in a framework-independent, testable way
