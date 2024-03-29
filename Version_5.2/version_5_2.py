# -*- coding: utf-8 -*-
"""version_5.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1igRV_b3D2Q9Q7FZKhD9HyreQNe7H5aPG
"""

import yfinance as yf
import pandas as pd

# Define the stocks and the period for data fetching
stocks = ['BAJFINANCE.NS', 'HDFCAMC.NS', 'ASIANPAINT.NS', 'TCS.NS', 'DRREDDY.NS']
start_date = '2013-01-01'  # Start date set to 10 years ago
end_date = '2023-01-01'    # End date set to the start of 2023

# Fetch data from Yahoo Finance
def fetch_data(ticker):
    """
    Fetches historical data for a given ticker from Yahoo Finance.
    :param ticker: Stock symbol.
    :return: DataFrame with historical data.
    """
    return yf.download(ticker, start=start_date, end=end_date)

# Get data for each stock
stock_data = {stock: fetch_data(stock) for stock in stocks}

#Displaying the first few rows of one of the stock data
print(stock_data['BAJFINANCE.NS'].head())

"""**Feature Engineering:[Indicators,sentiment Analysis,Nifty Trend]**"""

import pandas as pd

"""1. MACD Calculation
MACD is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA.
"""

def calculate_macd(data, slow=26, fast=12, signal=9):
    """
    Calculate MACD indicator.
    :param data: DataFrame with stock data.
    :param slow: Number of periods for slow EMA.
    :param fast: Number of periods for fast EMA.
    :param signal: Number of periods for signal line.
    :return: DataFrame with MACD columns added.
    """
    data['EMA12'] = data['Close'].ewm(span=fast, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=slow, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['MACD_Signal'] = data['MACD'].ewm(span=signal, adjust=False).mean()
    return data

"""2. RSI Calculation
RSI is calculated based on average gains and losses over a specified period, typically 14 days.


"""

def calculate_rsi(data, periods=14):
    """
    Calculate RSI indicator.
    :param data: DataFrame with stock data.
    :param periods: Number of periods to calculate RSI.
    :return: DataFrame with RSI column added.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

"""3. Bollinger Bands Calculation
Bollinger Bands consist of three lines: the middle band is a simple moving average (typically over 20 days), and the upper and lower bands are calculated as two standard deviations away from the middle band.
"""

def calculate_bollinger_bands(data, window=20, num_of_std=2):
    """
    Calculate Bollinger Bands.
    :param data: DataFrame with stock data.
    :param window: Moving average window size.
    :param num_of_std: Number of standard deviations for the bands.
    :return: DataFrame with Bollinger Bands columns added.
    """
    data['Middle_Band'] = data['Close'].rolling(window=window).mean()
    data['STD'] = data['Close'].rolling(window=window).std()
    data['Upper_Band'] = data['Middle_Band'] + (data['STD'] * num_of_std)
    data['Lower_Band'] = data['Middle_Band'] - (data['STD'] * num_of_std)
    return data

# Sample usage for one stock
sample_data = stock_data['BAJFINANCE.NS']
sample_data = calculate_macd(sample_data)
sample_data = calculate_rsi(sample_data)
sample_data = calculate_bollinger_bands(sample_data)

# Display the data with the new indicators
print(sample_data.head())

"""4.Fibonacci Retracement Levels
Fibonacci retracement levels are horizontal lines that indicate where support and resistance are likely to occur. They are based on Fibonacci numbers. We'll use the highest and lowest prices over the stock's recent period to calculate these levels.
"""

def calculate_fibonacci_retracement(data):
    """
    Calculate Fibonacci retracement levels.
    :param data: DataFrame with stock data.
    :return: DataFrame with Fibonacci levels added.
    """
    max_price = data['High'].max()
    min_price = data['Low'].min()
    diff = max_price - min_price
    data['Fibonacci_Level_1'] = max_price - 0.236 * diff
    data['Fibonacci_Level_2'] = max_price - 0.382 * diff
    data['Fibonacci_Level_3'] = max_price - 0.618 * diff
    return data

"""5.Average True Range (ATR)
ATR measures market volatility by decomposing the entire range of an asset price for that period. It's typically calculated over 14 days.
"""

def calculate_atr(data, period=14):
    """
    Calculate Average True Range (ATR).
    :param data: DataFrame with stock data.
    :param period: Period over which to calculate ATR.
    :return: DataFrame with ATR column added.
    """
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Close'].shift())
    data['Low-Close'] = abs(data['Low'] - data['Close'].shift())
    data['TR'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    data['ATR'] = data['TR'].rolling(window=period).mean()
    return data.drop(['High-Low', 'High-Close', 'Low-Close', 'TR'], axis=1)

# Looping through each stock's DataFrame and applying the calculations
for stock in stock_data:
    stock_data[stock] = calculate_macd(stock_data[stock])
    stock_data[stock] = calculate_rsi(stock_data[stock])
    stock_data[stock] = calculate_bollinger_bands(stock_data[stock])
    stock_data[stock] = calculate_fibonacci_retracement(stock_data[stock])
    stock_data[stock] = calculate_atr(stock_data[stock])

# Example usage for one stock
sample_data = stock_data['BAJFINANCE.NS']
sample_data = calculate_macd(sample_data)
sample_data = calculate_rsi(sample_data)
sample_data = calculate_bollinger_bands(sample_data)
sample_data = calculate_fibonacci_retracement(sample_data)
sample_data = calculate_atr(sample_data)

# Display the data with the new indicators
print(sample_data.head())

"""**Sentiment Analysis:** Fetching headlines"""

pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def fetch_yahoo_news_headlines(stock_symbol):
    """
    Fetch news headlines from Yahoo News for a given stock symbol.
    :param stock_symbol: Stock symbol for which to fetch news.
    :return: List of news headlines.
    """
    url = f"https://news.search.yahoo.com/search?p={stock_symbol}"
    headers = {'User-Agent': 'Mozilla/5.0'}  # User-Agent header to mimic a browser request
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []  # Return an empty list if there's an error fetching the page

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h4', class_='s-title')
    return [headline.get_text().strip() for headline in headlines]

# List of stocks
stocks = ['BAJFINANCE.NS', 'HDFCAMC.NS', 'ASIANPAINT.NS', 'TCS.NS', 'DRREDDY.NS']

# Fetch and print headlines for each stock
for stock in stocks:
    headlines = fetch_yahoo_news_headlines(stock)
    print(f"Headlines for {stock}:")
    for headline in headlines:
        print(f" - {headline}")
    print("\n")

"""**Sentiment Analysis:**"""

from textblob import TextBlob

def analyze_sentiment(headlines):
    """
    Analyze the sentiment of a list of headlines.
    :param headlines: List of news headlines.
    :return: Average polarity and subjectivity.
    """
    total_polarity = 0
    total_subjectivity = 0
    num_headlines = len(headlines)

    for headline in headlines:
        analysis = TextBlob(headline)
        total_polarity += analysis.sentiment.polarity
        total_subjectivity += analysis.sentiment.subjectivity

    # Avoid division by zero
    if num_headlines == 0:
        return 0, 0

    average_polarity = total_polarity / num_headlines
    average_subjectivity = total_subjectivity / num_headlines
    return average_polarity, average_subjectivity



# Perform sentiment analysis for each stock
for stock in stocks:
    headlines = fetch_yahoo_news_headlines(stock)
    average_polarity, average_subjectivity = analyze_sentiment(headlines)
    print(f"Sentiment Analysis for {stock}:")
    print(f" - Average Polarity: {average_polarity}")
    print(f" - Average Subjectivity: {average_subjectivity}")
    print("\n")

""" add two new columns to each of these datasets: sentiment_polarity and sentiment_subjectivity."""

# Sentiment scores from your analysis
sentiment_scores = {
    'BAJFINANCE.NS': {'polarity': 0, 'subjectivity': 0},
    'HDFCAMC.NS': {'polarity': 0, 'subjectivity': 0},
    'ASIANPAINT.NS': {'polarity': 0.12166666666666667, 'subjectivity': 0.13666666666666666},
    'TCS.NS': {'polarity': 0.020833333333333336, 'subjectivity': 0.2458333333333333},
    'DRREDDY.NS': {'polarity': 0, 'subjectivity': 0}
}

# Add the sentiment scores to each stock's DataFrame
for stock, scores in sentiment_scores.items():
    stock_data[stock]['sentiment_polarity'] = scores['polarity']
    stock_data[stock]['sentiment_subjectivity'] = scores['subjectivity']

# Example: Print the updated DataFrame for one stock
print(stock_data['TCS.NS'].head())

print(stock_data['TCS.NS'].head())

"""**Calculating Nifty Trend:**"""

import yfinance as yf

# Fetch Nifty data
nifty_data = yf.download('^NSEI', start='2013-01-01', end='2023-01-01')

nifty_data = calculate_macd(nifty_data)
nifty_data = calculate_rsi(nifty_data)
nifty_data = calculate_bollinger_bands(nifty_data)
nifty_data = calculate_fibonacci_retracement(nifty_data)
nifty_data = calculate_atr(nifty_data)

"""**Merge Nifty Data with Each Stock's Data**"""

for stock in stock_data:
    # Merge on the 'Date' column
    stock_data[stock] = stock_data[stock].merge(nifty_data, on='Date', how='left', suffixes=('', '_nifty'))

# Example check
print(stock_data['BAJFINANCE.NS'].head())

"""**Dropping NAN rows:**"""

for stock in stock_data:
    stock_data[stock].dropna(inplace=True)

print(stock_data['BAJFINANCE.NS'].head())

# Assuming each DataFrame in stock_data has columns for 'Close', 'MACD', 'RSI', etc.

for stock, df in stock_data.items():
    # 1. Calculate Expected Returns - Simple Moving Average of past weekly returns
    df['Weekly_Return'] = df['Close'].pct_change(periods=5)  # 5 days for a week
    df['Expected_Return'] = df['Weekly_Return'].rolling(window=5).mean()

    # 2. Assess Risk - Standard Deviation of weekly returns
    df['Risk'] = df['Weekly_Return'].rolling(window=5).std()

    # 3. Evaluate Indicator Positivity - Example: MACD
    df['Indicator_Score'] = np.where(df['MACD'] > df['MACD_Signal'], 1, -1)

    # 4. Composite Performance Score
    # Adjust weights as necessary
    df['Composite_Score'] = df['Expected_Return'] - df['Risk'] + df['Indicator_Score']

# 5. Identifying the Best Stock
combined_df = pd.concat(stock_data.values())
best_stocks_weekly = combined_df.groupby(combined_df.index)['Composite_Score'].idxmax()
combined_df['Target'] = combined_df.index.isin(best_stocks_weekly).astype(int)

# Separate the combined DataFrame back into individual stocks
for stock in stock_data.keys():
    stock_data[stock] = combined_df[combined_df['Stock'] == stock]

"""**Add Stock Label and Concatenate All DataFrames**"""

import pandas as pd

# Assuming stock_data is your dictionary of DataFrames
combined_df = pd.DataFrame()

for stock, df in stock_data.items():
    df['Stock'] = stock  # Add a column for the stock label
    combined_df = pd.concat([combined_df, df])  # Concatenate to the combined DataFrame

print(combined_df.columns.tolist())

from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Select features for the LSTM model, excluding the target and non-numeric columns
features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'EMA12', 'EMA26', 'MACD', 'MACD_Signal', 'RSI',
            'Middle_Band', 'STD', 'Upper_Band', 'Lower_Band', 'Fibonacci_Level_1', 'Fibonacci_Level_2', 'Fibonacci_Level_3',
            'ATR', 'sentiment_polarity', 'sentiment_subjectivity', 'Open_nifty', 'High_nifty', 'Low_nifty',
            'Close_nifty', 'Adj Close_nifty', 'Volume_nifty', 'EMA12_nifty', 'EMA26_nifty', 'MACD_nifty',
            'MACD_Signal_nifty', 'RSI_nifty', 'Middle_Band_nifty', 'STD_nifty', 'Upper_Band_nifty', 'Lower_Band_nifty',
            'Fibonacci_Level_1_nifty', 'Fibonacci_Level_2_nifty', 'Fibonacci_Level_3_nifty', 'ATR_nifty']

X = combined_df[features]
y = combined_df['Target']

# Normalize Features
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

# Convert Data to Time Series Format
def create_dataset(X, y, time_steps=1):
    Xs, ys = [], []
    for i in range(len(X) - time_steps):
        Xs.append(X[i:(i + time_steps)])
        ys.append(y.iloc[i + time_steps])
    return np.array(Xs), np.array(ys)

time_steps = 60  # use 60 days of historical data
X_series, y_series = create_dataset(pd.DataFrame(X_scaled), y, time_steps)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_series, y_series, test_size=0.2, random_state=42)

# LSTM Model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(25))
model.add(Dense(1, activation='sigmoid'))  # Sigmoid for binary classification

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.1)

"""**Evaluating the Model:**"""

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy}")