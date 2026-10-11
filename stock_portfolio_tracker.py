"""Stock Portfolio Tracker — educational internship project."""
from datetime import datetime
import pandas as pd

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False


def get_current_price(ticker, fallback_price):
    """Return latest available close price, or the supplied sample price."""
    if YFINANCE_AVAILABLE:
        try:
            history = yf.Ticker(ticker).history(period="5d")
            if not history.empty:
                prices = history["Close"].dropna()
                if not prices.empty:
                    return float(prices.iloc[-1]), "Yahoo Finance"
        except Exception as error:
            print(f"Could not retrieve {ticker}: {error}")
    return float(fallback_price), "Sample price"


def main():
    portfolio = pd.DataFrame([
        {"ticker": "AAPL", "company": "Apple", "shares": 5, "purchase_price": 180.00, "sample_current_price": 190.00},
        {"ticker": "MSFT", "company": "Microsoft", "shares": 3, "purchase_price": 400.00, "sample_current_price": 420.00},
        {"ticker": "GOOGL", "company": "Alphabet", "shares": 4, "purchase_price": 150.00, "sample_current_price": 145.00},
    ])

    price_results = portfolio.apply(
        lambda row: get_current_price(row["ticker"], row["sample_current_price"]), axis=1
    )
    portfolio["current_price"] = [item[0] for item in price_results]
    portfolio["price_source"] = [item[1] for item in price_results]
    portfolio["purchase_cost"] = portfolio["shares"] * portfolio["purchase_price"]
    portfolio["current_value"] = portfolio["shares"] * portfolio["current_price"]
    portfolio["profit_loss"] = portfolio["current_value"] - portfolio["purchase_cost"]
    portfolio["return_percent"] = portfolio["profit_loss"] / portfolio["purchase_cost"] * 100

    print("STOCK PORTFOLIO SUMMARY")
    print("=" * 30)
    print(f"Report date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(portfolio[["ticker", "company", "shares", "purchase_cost", "current_value",
                     "profit_loss", "return_percent", "price_source"]].round(2).to_string(index=False))
    invested = portfolio["purchase_cost"].sum()
    current_value = portfolio["current_value"].sum()
    profit_loss = current_value - invested
    overall_return = profit_loss / invested * 100 if invested else 0
    print(f"\nTotal invested: ${invested:,.2f}")
    print(f"Current value:  ${current_value:,.2f}")
    print(f"Profit/loss:    ${profit_loss:,.2f}")
    print(f"Overall return: {overall_return:.2f}%")
    portfolio.to_csv("portfolio_report.csv", index=False)
    print("\nSaved portfolio_report.csv")


if __name__ == "__main__":
    main()
