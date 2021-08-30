import pandas as pd
import pickle as pkl

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
    