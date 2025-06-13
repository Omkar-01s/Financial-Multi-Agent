import yfinance as yf
import plotly.graph_objects as go


def plot_stock_price(ticker: str):

    df = yf.Ticker(ticker).history(period="1mo")


    if df.empty:
        raise ValueError(f"No stock data found for ticker: {ticker}")


    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index, 
            y=df["Close"], 
            mode='lines+markers', 
            name='Close Price',
            line=dict(color='blue')
        )
    )

    fig.update_layout(
        title=f"{ticker.upper()} - 1 Month Stock Price Chart",
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        template='plotly_white'
    )

    return fig
