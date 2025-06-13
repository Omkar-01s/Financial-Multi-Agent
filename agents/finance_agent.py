import yfinance as yf 
from langchain import Tool

def get_stock_data(ticker -str) -> str:
    stock.yf.ticker()
    df = stock.history(period="1mo")
    if df.empty:
        return f"No data found for {ticker}"
    return df.tail().to_markdown()


finance_tool = Tool(
    name="Finance Agent",
    func=lambda ticker: get_stock_data(ticker.strip().upper()), 
    description=(
        "Useful when you need to retrieve the past 1-month stock price history of a public company. "
        "Provide a valid stock ticker symbol like 'AAPL', 'MSFT', or 'TSLA'. "
        "Returns the latest historical stock data as a table."
    )
)
