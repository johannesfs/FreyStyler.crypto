import pandas as pd
import pickle as pkl
import numpy as np
import os


data_dir = "./data"
markets = ["Kraken"]
fx_pairs = ["BTCUSD", "ETHUSD", "ALGOUSD", "STORJUSD", "MANAUSD"]

def main(**kwargs):

	for mkt in markets:
		for pair in fx_pairs:
			df = pd.read_csv(f"{data_dir}/{mkt}_{pair}_day.csv")
			df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
			df.set_index("date", inplace=True)
			
			df["returns"] = df["close"].pct_change() + 1
			df.returns.fillna(1, inplace=True)
			df["log_returns"] = np.log(df["returns"])
			
			with open(f"notebooks/data/{mkt}_{pair}.pkl", "wb") as file:
				pkl.dump(df, file)
			

if __name__ == '__main__':
	main()