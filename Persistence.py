from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

import pyodbc

engine = create_engine("mysql+pyodbc://freystyler:freestyle@localhost/Crypto?charset=utf8mb4")

Base = declarative_base()

class CryptoCurrencyPair(Base):
	__tablename__ = 'CryptoCurrencyPair'

	id = Column(Integer, primary_key=True)
	name = Column(String(45))
	quotecurrency = Column(String(5))
	basecurrency = Column(String(5))
	description = Column(Text(128))

	def __repr__(self):
		return "<CryptoCurrencyPair(name='%s', pair='%s/%s')>" % (self.name, self.quotecurrency, self.basecurrency)

class QuoteMap(Base):
	__tablename__ = 'QuoteMap'

	quoteref = Column(Integer, primary_key=True)
	cryptocurrencyid = Column(Integer, ForeignKey('CryptoCurrencyPair.id'))
	datafield = Column(String(64))
	market = Column(String(45))

	def __repr__(self):
		return "<CryptoCurrencyPair(name='%s', pair='%s/%s')>" % (self.name, self.quotecurrency, self.basecurrency)

class QuoteHistory(Base):
	__tablename__ = 'QuoteHistory'

	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime)
	quote = Column()

if __name__ == '__main__':
	print(CryptoCurrencyPair.__table__)
	#QuoteMap.__table__

