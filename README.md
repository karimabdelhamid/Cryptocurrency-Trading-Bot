# Cryptocurrency Trading Bot

This project represents a simple yet powerful cryptocurrency trading bot focused on Bitcoin, showcasing real-time market data fetching, sophisticated data analysis, and automated decision-making. The bot is designed to simulate trading strategies based on historical price data and real-time price information, offering insights into the potential of automated trading systems.

## Features

- **Real-Time Data Fetching**: Utilizes the CoinGecko API to fetch real-time Bitcoin prices, ensuring the bot makes decisions based on the most current market conditions.
- **Historical Data Analysis**: Gathers the last 30 days of Bitcoin price data to calculate a Simple Moving Average (SMA), demonstrating the bot's ability to analyze trends over time.
- **Automated Trading Decisions**: Based on the comparison of current prices to historical averages, the bot decides whether to "buy" or "sell," simulating an automated trading strategy.
- **Python-Based**: Written in Python, a leading programming language in data science and automation, highlighting the project's foundation on accessible, powerful technology.

## Practical Applications

This bot serves as a prototype for more sophisticated trading algorithms, showcasing the potential to leverage historical data and real-time information for market analysis and automated decision-making. Its practical applications extend to:

- **Financial Analysis**: Demonstrates how to process and analyze financial data, a valuable skill in many tech-driven finance roles.
- **Data Science Projects**: Offers a foundation for projects involving time series data, trend analysis, and predictive modeling.
- **Educational Tool**: Serves as an educational example of interacting with APIs, handling data in Python, and applying basic financial concepts in programming.

## Technologies Used

- **Python**: For the core algorithm and data processing.
- **Requests Library**: To handle HTTP requests to the CoinGecko API.
- **Datetime & Timedelta**: For managing dates and times, crucial for fetching historical data.

## How to Run

To run this project, you will need Python installed on your system along with the `requests` library. You can install the required library using the following command:

```bash
pip install requests
```

After installing the necessary library, simply clone this repository and run the main script:

```bash
python main.py
```
## How It Works

- **Fetches Real-Time Price**: The bot starts by fetching the current price of Bitcoin using the CoinGecko API.
- **Analyzes Historical Prices**: It then retrieves the last 30 days of price data to calculate the SMA, providing a basis for comparison.
- **Makes a Decision**: Based on the SMA and the current price, the bot decides whether the market condition is favorable for buying or selling.
- **Simulates a Trade**: Though this bot simulates decisions, it lays the groundwork for implementing actual trading commands through exchange APIs.

## Future Directions

While this bot currently operates on a basic level, future enhancements could include more complex trading strategies, risk management features, and real-time trading capabilities. Integrating machine learning models to predict price movements and incorporating a wider range of indicators could significantly increase its sophistication and potential profitability.
