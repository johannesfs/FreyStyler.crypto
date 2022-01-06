import pandas as pd
import pickle as pkl
import numpy as np
import re

from os import listdir
from os.path import isfile, join

data_dir = "./data"
markets = ["Kraken"]
fx_pairs = ["BTCUSD", "ETHUSD", "ALGOUSD", "STORJUSD", "MANAUSD"]

def main(**kwargs):

	pairs = []
	onlyfiles = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]
	for price_file in onlyfiles:

		df = pd.read_csv(f"{data_dir}/{price_file}")
		pair = re.split(r'_', price_file)[1]
		print(pair)
		pairs.append(pair[:-3])
		df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
		df.set_index("date", inplace=True)
		
		df["returns"] = df["close"].pct_change() + 1
		df.returns.fillna(1, inplace=True)
		df["log_returns"] = np.log(df["returns"])
			
		with open(f"notebooks/data/{price_file[:-4]}.pkl", "wb") as file:
			pkl.dump(df, file)
	
	with open(f"notebooks/data/pairs.pkl", "wb") as pairs_file:
		pkl.dump(pairs, pairs_file)

			

if __name__ == '__main__':
	main()