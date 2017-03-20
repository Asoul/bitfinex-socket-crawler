import time

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from tools import config

# Database settings
engine = create_engine(config.DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Ticker(object):
    timestamp = sa.Column(sa.BigInteger, primary_key=True)
    bid_price = sa.Column(sa.Float)
    bid_size = sa.Column(sa.Float)
    ask_price = sa.Column(sa.Float)
    ask_size = sa.Column(sa.Float)
    daily_change = sa.Column(sa.Float)
    daily_change_perc = sa.Column(sa.Float)
    last_price = sa.Column(sa.Float)
    daily_volume = sa.Column(sa.Float)
    daily_high = sa.Column(sa.Float)
    daily_low = sa.Column(sa.Float)

    def __init__(self, data):
        self.timestamp = int(time.time() * 1000000)
        self.bid_price = data[0]
        self.bid_size = data[1]
        self.ask_price = data[2]
        self.ask_size = data[3]
        self.daily_change = data[4]
        self.daily_change_perc = data[5]
        self.last_price = data[6]
        self.daily_volume = data[7]
        self.daily_high = data[8]
        self.daily_low = data[9]

class BTCTicker(Ticker, Base):
    __tablename__ = 'btc_ticker'

class ETHTicker(Ticker, Base):
    __tablename__ = 'eth_ticker'

class ETCTicker(Ticker, Base):
    __tablename__ = 'etc_ticker'

class BFXTicker(Ticker, Base):
    __tablename__ = 'bfx_ticker'

class ZECTicker(Ticker, Base):
    __tablename__ = 'zec_ticker'

class XMRTicker(Ticker, Base):
    __tablename__ = 'xmr_ticker'

class LTCTicker(Ticker, Base):
    __tablename__ = 'ltc_ticker'

class DSHTicker(Ticker, Base):
    __tablename__ = 'dsh_ticker'

class RRTTicker(Ticker, Base):
    __tablename__ = 'rrt_ticker'

class BCCTicker(Ticker, Base):
    __tablename__ = 'bcc_ticker'

class BCUTicker(Ticker, Base):
    __tablename__ = 'bcu_ticker'
