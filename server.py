import json
import time
import sys
from multiprocessing import Process, Manager

import websocket

from tools.config import CURRENCY_LIST
from tools.logger import log, log_err, exception_dump
from tools.database import Session, BTCTicker, ETHTicker, ETCTicker, BFXTicker,\
    ZECTicker, XMRTicker, LTCTicker, DSHTicker, RRTTicker, BCCTicker, BCUTicker

channel_map = {}
ticker_class_map = {
    'BTCUSD': BTCTicker,
    'ETHUSD': ETHTicker,
    'ETCUSD': ETCTicker,
    'BFXUSD': BFXTicker,
    'ZECUSD': ZECTicker,
    'XMRUSD': XMRTicker,
    'LTCUSD': LTCTicker,
    'DSHUSD': DSHTicker,
    'RRTUSD': RRTTicker,
    'BCCUSD': BCCTicker,
    'BCUUSD': BCUTicker
}

# Shared memory between process
manager = Manager()
last_heart_beat_map = manager.dict()
checker_process = None

def check_heart_beat(ws):
    should_exit = False
    while not should_exit:
        time.sleep(10)
        now = time.time()
        for _, last_tick in last_heart_beat_map.items():
            # If 10 seconds a topic missed, then should reconnect
            if now - last_tick > 10:
                log('Not got pong, exit process')
                ws.close()
                should_exit = True


def on_message(ws, data):
    try:
        payload = json.loads(data)
        if isinstance(payload, dict):
            # {"event":"subscribed","channel":"ticker","chanId":23,"pair":"BTCUSD"}
            if payload['event'] == 'subscribed':
                if payload['channel'] == 'ticker':
                    channel_map[payload['chanId']] = ticker_class_map[payload['pair']]
                    last_heart_beat_map[payload['chanId']] = time.time()

        elif isinstance(payload, list):
            if payload[0] not in channel_map:
                raise KeyError

            last_heart_beat_map[payload[0]] = time.time()

            if payload[1] == 'hb':
                return

            target_class = channel_map[payload[0]]
            new_object = target_class(payload[1:])
            session = Session()
            session.add(new_object)
            session.commit()
            session.close()
        else:
            log_err(type(payload))
    except Exception:
        exception_dump()
        log_err(data)


def on_error(ws, error):
    log('error', error, file=sys.stderr)

def on_close(ws):
    if checker_process:
        checker_process.join(3)
    log("### closed ###")

def on_open(ws):
    log("### opened ###")

    # Ticker
    for currency in CURRENCY_LIST:
        ws.send('{"event":"subscribe", "channel":"ticker", "pair":"' + currency + 'USD"}')
        # ws.send('{"event":"subscribe", "channel":"trades", "pair":"' + currency + 'USD"}')
        # ws.send('{"event":"subscribe", "channel":"book", "pair":"' + currency + 'USD", "prec":"P0", "freq":"F0"}')

    # Health Beat
    global checker_process
    checker_process = Process(target=check_heart_beat, args=(ws,))
    checker_process.start()

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.run_forever()
