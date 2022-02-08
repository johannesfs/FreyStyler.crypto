# First import the libraries that we need to use
import pandas as pd
import requests
import json
import os
import logging

data_dir = "/tmp/crypto_data"
url_base = "https://api.kraken.com/0/public/"
timeframes = {"minute": 1, "hour": 60, "day": 1440}
currencies = {"crypto":[
    "BTC","ETH","ADA","USDT","XRP","DOGE","USDC","DOT","SOL","UNI",
"BCH","LTC","LINK","WBTC","MATIC","XLM","ETC","FIL","TRX","DAI","XMR", "AKT",
"AAVE","EOS","AXS","GRT","ATOM","XTZ","MKR","ALGO","WAVES", "SDN",
"DASH","KSM","COMP","CHZ","ZEC","MANA","ENJ","SUSHI",
"SNX","YFI","FLOW","BAT","QTUM","SC","BNT","PERP","ZRX","ICX","CRV","OMG","NANO",
"ANKR","LRC","KAVA","SAND","MINA","REN","1INCH","LSK",
"OCEAN","GNO","STORJ","LPT","INJ","OGN","KNC","PAXG",
"SRM","EWT","BAND","REP","REPV2","CTSI","MIR","OXT","KEEP","MLN","BADGER","ANT",
"BAL","GHST","CQT","KAR","TBTC", "RARI"],
"fiat":
    ["USD","JPY","BGN","CYP","CZK","DKK","EEK","GBP","HUF","LTL",
"LVL","MTL","PLN","ROL","RON","SEK","SIT","SKK","CHF","ISK","NOK","HRK","RUB",
"TRL","TRY","AUD","BRL","CAD","CNY","HKD","IDR","ILS","INR","KRW","MXN","MYR",
"NZD","PHP","SGD","THB","ZAR"]}

def main(**kwargs):
    """Kraken - More generic function"""

    FORMAT = '%(asctime)s [%(levelname)s]: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    symbol = kwargs.get('symbol', "BTC")
    data_type = kwargs.get('data_type', "OHLC") # OHLC, Spread, Trades
    timeframe = kwargs.get('timeframe', "day")

    logging.info(f"Collection {symbol} data from Kraken")
    symbol = symbol.upper() + "USD"
    if data_type == "OHLC":
        url = f'{url_base}/OHLC?pair={symbol}&interval={timeframes[timeframe]}'
    else:
        url = f'{url_base}/{data_type}?pair={symbol}'

    response = requests.get(url)
    if response.status_code == 200:  # check to make sure the response from server is good
        j = json.loads(response.text)
        result = j['result']
        keys = []
        for item in result:
            keys.append(item)
        if keys[0] != 'last':
            data = pd.DataFrame(result[keys[0]],
                                columns=['unix', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'tradecount'])
        else:
            data = pd.DataFrame(result[keys[1]],
                                columns=['unix', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'tradecount'])

        data['date'] = pd.to_datetime(data['unix'], unit='s')
        data['volume_from'] = data['volume'].astype(float) * data['close'].astype(float)

        if data is None:
            logging.warning("Did not return any data from Kraken for this symbol")
        else:
            os.makedirs(data_dir, mode=0o777, exist_ok=True)
            data.to_csv(f'{data_dir}/Kraken_{symbol}_{timeframe}.csv', index=False)
    else:
        logging.critical("Did not receieve OK response from Kraken API")

def fetch_OHLC_data(symbol, timeframe):
    """This function will get Open/High/Low/Close, Volume and tradecount data for the pair passed and save to CSV"""
    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/USD
    symbol = pair_split[0] + pair_split[1]
    url = f'{url_base}/OHLC?pair={symbol}&interval={timeframe}'
    response = requests.get(url)

    if response.status_code == 200:  # check to make sure the response from server is good
        j = json.loads(response.text)
        result = j['result']
        keys = []
        for item in result:
            keys.append(item)
        if keys[0] != 'last':
            data = pd.DataFrame(result[keys[0]],
                                columns=['unix', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'tradecount'])
        else:
            data = pd.DataFrame(result[keys[1]],
                                columns=['unix', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'tradecount'])

        data['date'] = pd.to_datetime(data['unix'], unit='s')
        data['volume_from'] = data['volume'].astype(float) * data['close'].astype(float)

        # if we failed to get any data, print an error...otherwise write the file
        if data is None:
            logging.warning("Did not return any data from Kraken for this symbol")
        else:
            if timeframe == '1':
                tf = 'minute'
            elif timeframe == '60':
                tf = 'hour'
            elif timeframe == '1440':
                tf = 'day'
            else:
                tf = ''
            data.to_csv(f'{data_dir}/Kraken_{symbol}_{tf}.csv', index=False)
    else:
        logging.critical("Did not receieve OK response from Kraken API")

def fetch_SPREAD_data(symbol):
    """This function will return the nearest bid/ask and calculate the spread for the symbol passed and save
        the results to a CSV file"""
    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/USD
    symbol = pair_split[0] + pair_split[1]
    url = f'{url_base}/Spread?pair={symbol}'
    response = requests.get(url)

    if response.status_code == 200:  # check to make sure the response from server is good
        j = json.loads(response.text)
        result = j['result']
        keys = []
        for item in result:
            keys.append(item)
        if keys[0] != 'last':
            data = pd.DataFrame(result[keys[0]], columns=['unix', 'bid', 'ask'])
        else:
            data = pd.DataFrame(result[keys[1]], columns=['unix', 'bid', 'ask'])

        data['date'] = pd.to_datetime(data['unix'], unit='s')
        data['spread'] = data['ask'].astype(float) - data['bid'].astype(float)

        # if we failed to get any data, print an error...otherwise write the file
        if data is None:
            logging.warning("Did not return any data from Kraken for this symbol")
        else:
            data.to_csv(f'{data_dir}/Kraken_{symbol}_spreads.csv', index=False)
    else:
        logging.critical("Did not receieve OK response from Kraken API")

def fetch_PRINTS_data(symbol):
    """This function will return historical trade prints for the symbol passed and save the results to a CSV file"""
    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/USD
    symbol = pair_split[0] + pair_split[1]
    url = f'{url_base}/Trades?pair={symbol}'
    response = requests.get(url)
    if response.status_code == 200:  # check to make sure the response from server is good
        j = json.loads(response.text)

        result = j['result']
        keys = []
        for item in result:
            keys.append(item)
        if keys[0] != 'last':
            data = pd.DataFrame(result[keys[0]], columns=['price', 'volume', 'time', 'buysell', 'ordtype', 'misc'])
        else:
            data = pd.DataFrame(result[keys[1]], columns=['price', 'volume', 'time', 'buysell', 'ordtype', 'misc'])

        data['date'] = pd.to_datetime(data['time'], unit='s')
        data['buysell'] = data['buysell'].apply(lambda x: "buy" if x == 'b' else "sell")
        data['ordtype'] = data['ordtype'].apply(lambda x: "limit" if x == 'l' else "market")
        data['dollaramount'] = data['price'].astype(float) * data['volume'].astype(float)
        data.drop(columns=['misc'], inplace=True)  #drop misc column that is typically blank

        # if we failed to get any data, print an error...otherwise write the file
        if data is None:
            logging.warning("Did not return any data from Kraken for this symbol")
        else:
            data.to_csv(f'{data_dir}/Kraken_{symbol}_tradeprints.csv', index=False)
    else:
        logging.critical("Did not receieve OK response from Kraken API")

def fetch_daily_data(symbol):
    """Coinbase"""

    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/EUR
    symbol = pair_split[0] + '-' + pair_split[1]
    url = f'https://api.pro.coinbase.com/products/{symbol}/candles?granularity=86400'
    response = requests.get(url)
    if response.status_code == 200:  # check to make sure the response from server is good
        data = pd.DataFrame(json.loads(response.text), columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
        data['date'] = pd.to_datetime(data['unix'], unit='s')  # convert to a readable date
        data['vol_fiat'] = data['volume'] * data['close']      # multiply the BTC volume by closing price to approximate fiat volume

        # if we failed to get any data, print an error...otherwise write the file
        if data is None:
            logging.warning("Did not return any data from Coinbase for this symbol")
        else:
            data.to_csv(f'Coinbase_{pair_split[0] + pair_split[1]}_dailydata.csv', index=False)

    else:
        logging.critical("Did not receieve OK response from Coinbase API")


if __name__ == "__main__":
    # we set which pair we want to retrieve data for
    for pair in currencies["crypto"]:
        main(symbol=pair)

    #pair = "ALGO/USD"
    # full timeframe intervals found here: https://www.kraken.com/en-us/features/api#get-ohlc-data
    #fetch_OHLC_data(symbol=pair, timeframe='1') # fetches minute data
    # fetch_OHLC_data(symbol=pair, timeframe='60')  # fetches hourly data
    #fetch_OHLC_data(symbol=pair, timeframe='1440')  # fetches daily data
    #fetch_SPREAD_data(symbol=pair) # gets bid/ask spread data
    #fetch_PRINTS_data(symbol=pair) # gets historical trade print data


                 