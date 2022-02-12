from sqlalchemy import BigInteger, Numeric, create_engine, Enum, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

import pyodbc

engine = create_engine("mysql+pyodbc://freystyler:freestyle@localhost/Crypto?charset=utf8mb4")


Base = declarative_base()

class CurrencyPair(Base):
	__tablename__ = 'CurrencyPair'

	id = Column(Integer, primary_key=True)
	name = Column(String(45), nullable=False)
	quotecurrency = Column(BigInteger(8), ForeignKey('Currency.id'), nullable=False)
	basecurrency = Column(BigInteger(8), ForeignKey('Currency.id'), nullable=False)
	description = Column(Text(128))

	def __repr__(self):
		return "<CurrencyPair(name='%s', pair='%s/%s')>" % (self.name, self.quotecurrency, self.basecurrency)

class QuoteMap(Base):
	__tablename__ = 'QuoteMap'

	quoteref = Column(Integer, primary_key=True)
	currencyid = Column(Integer, ForeignKey('CurrencyPair.id'), nullable=False)
	datafield = Column(String(64), nullable=False)
	market = Column(String(45))

	def __repr__(self):
		return "<CurrencyPair(name='%s', pair='%s/%s')>" % (self.name, self.quotecurrency, self.basecurrency)

class QuoteHistory(Base):
	__tablename__ = 'QuoteHistory'

	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime, nullable=False)
	quote = Column(Numeric, nullable=False)
	quoteref = Column(BigInteger(8), ForeignKey('QuoteMap.quoteref'), nullable=False)

class Currency(Base):
	__tablename__ = 'Currency'

	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)
	currencycode = Column(String(4), nullable=False)
	currencytype = Column(Enum, nullable=False)


if __name__ == '__main__':
	print(CurrencyPair.__table__)
	#QuoteMap.__table__

