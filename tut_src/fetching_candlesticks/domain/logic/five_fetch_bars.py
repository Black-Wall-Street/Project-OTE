from datetime import datetime, timedelta
from domain.models.one_asset import Asset, AssetType
from domain.adapters.four_yf_market_data_adapter import YFMarketDataAdapter
import time

def main():
    print("Hexagonal Architecture Demo — Fetching Market Data")

    # Step 1: Define the asset
    asset = Asset(asset_type=AssetType.FOREX, symbol="EURUSD", currency="USD")
    # For forex: format symbol as 'EUR/USD'
    formatted = (
        f"{asset.symbol[:3]}/{asset.symbol[3:]}" 
        if asset.asset_type == AssetType.FOREX and len(asset.symbol) == 6
        else asset.symbol
    )

    print(f"\nAsset defined: {formatted} ({asset.asset_type.name})")

    # Step 2: Create adapter
    adapter = YFMarketDataAdapter(asset)
    print(f"Adapter created: {adapter.__class__.__name__}")

    # Step 3: Request historical data
    end_date = datetime.today()
    start_date = end_date - timedelta(days=5)
    adapter.request_historical_data(asset, start_date, end_date)

    # Step 4: Stream bars one by one
    print("\nStreaming bars:")
    while True:
        bar = adapter.next_bar(asset)
        if bar is None:
            break
        print(f"{bar.timestamp} | {bar.open:.4f} → {bar.close:.4f} | H: {bar.high:.4f}, L: {bar.low:.4f}, V: {bar.volume:.0f}")
        time.sleep(2.5)

    print("\nEnd of data stream.")

if __name__ == "__main__":
    main()
