import pandas as pd
import pickle as pkl
import numpy as np

short_window = 21
long_window = 84


with open("notebooks/Kraken_BTCUSD.pkl", "rb") as file:
    btc_kraken = pkl.load(file)
with open("notebooks/Kraken_ETHUSD.pkl", "rb") as file:
    eth_kraken = pkl.load(file)

def calc_performance(signal, returns):
    returns = returns[long_window:]
    daily_returns = returns*np.sign(signal)+1
    return daily_returns.cumprod()

def get_momentum_signal(log_returns):
    signal = log_returns["log_returns"].rolling(window=short_window).mean() - log_returns["log_returns"].rolling(window=long_window).mean()
    signal = signal[long_window:]
    signal[signal<=0] = 0
    return signal

if __name__ == "__main__":
    pass


# http://epchan.blogspot.com
# The Base Features are constructed using Binance’s dollar bar data, which includes:

# Open
# High
# Low
# Close
# Volume
# Order flow (sum of signed volumes) 
# +ve volume for buy aggressor tag and -ve volume for sell aggressor tag
# Buy market order value (sum of volumes corresponding to buy aggressor tag)
# Sell market order value (sum of volumes corresponding to sell aggressor tag)
# Base Features are based on:

# Relations between the price, the high price, the low price.
# Relative High: High Price relative to Open Price.
# Relative Low: Low Price relative to Open Price.
# Relative Close: Close Price relative to Open Price.
# Relative Volume: Buy orders relative to total absolute volume.
# Target Effort: computes an estimation of the “effort” that the price has to produce to reach the target price by comparing the observed low price and high price.
# Volume exchanged.
# Dollar Speed: Average signed quantity of dollars exchanged per second.
# Relations and potential correlations among the variations of the price, the order flow and the intensity of the activity in the market.
# Kyle’s Lambda: Relation between price change and orderflow.
# SCOF: Correlation of Order Flow with its lagged series.
# VPIN: Volume-synchronized probability of informed trading. 
# Volatility observed.
# VLT: Volatility of the returns (Exponentially Weighted)
    