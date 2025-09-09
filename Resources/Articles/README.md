# Literature Review on Algorithmic Trading

## 1. Sentiment-Driven and Technical Trading
📃 **[Enhancing Trading Performance Through Sentiment Analysis](https://arxiv.org/pdf/2507.09739)**  
This study integrates real-time sentiment analysis using GPT-2 and FinBERT with traditional technical indicators (like MACD, SAR, VW MACD) and time-series forecasting models (e.g., ARIMA, ETS) to enhance trading strategies on the S&P 500. The combined sentiment-driven and technical approach significantly outperforms a benchmark buy-and-hold strategy, delivering the top return of ~5.77%, and demonstrates more adaptive performance in volatile markets.

## 2. Randomness vs. Technical Strategies in Retail Trading
📃 **[The Retail FX Trader: Rising Above Random](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2817271)**  
This paper “The Retail FX Trader: Rising Above Random” by Chris Davison explores whether typical retail forex traders can outperform random trading by applying popular technical analysis strategies and disciplined risk-reward practices. It finds that while most traders underperform, using larger profit targets relative to allowed losses and even purely random entries can yield better than random outcomes.

📃 **[RANDOM STRATEGY VERSUS TECHNICAL ANALYSIS STRATEGY: THE CASE OF EUR/USD INTRADAY TRADING](https://www.researchgate.net/publication/343095098_RANDOM_STRATEGY_VERSUS_TECHNICAL_ANALYSIS_STRATEGY_THE_CASE_OF_EURUSD_INTRADAY_TRADING)**  
This paper by Svoboda & Sponerová compares a simple moving-average–based technical analysis strategy (with a 3:1 risk-reward ratio) against a timing-based random entry strategy across three years of EUR/USD intraday data, and finds that the random-timed approach may perform comparably, or even better, than the technical-analysis strategy under those conditions.

## 3. Transaction Costs estimation from OHLC Data
📃 **[Efficient Estimation of Bid-Ask Spreads from OHLC Prices](https://www.sciencedirect.com/science/article/pii/S0304405X24001399)**  
This paper by Ardia, Guidotti, and Kroencke suggests a strategy to estimate bid ask spreads using only open, high, low, and close (OHLC) data. The approach is asymptotically unbiased under discrete trading, combines OHLC information efficiently, and provides variance estimates to construct confidence intervals through formula 15. This allows practitioners to model transaction costs more realistically in backtests using either point estimates or conservative upper bound spreads without requiring direct quote data.
