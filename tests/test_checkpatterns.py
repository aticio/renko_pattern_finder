from pbrenko import PbRenko
from renko_pattern_finder import RenkoPatternFinder
import requests

BINANCE_URL = "https://api.binance.com/api/v3/klines"
SYMBOL = "BTCUSDT"
INTERVAL = "1d"
LIMIT = 365
PARAMS = {"symbol": SYMBOL, "interval": INTERVAL, "limit": LIMIT}


def test_checkpattern():
    response = requests.get(url=BINANCE_URL, params=PARAMS)
    data = response.json()
    close = [float(c[4]) for c in data]

    pbrnk = PbRenko(1, close)
    pbrnk.create_pbrenko()

    renko_pf = RenkoPatternFinder(pbrnk.bricks)
    renko_pf.check_patterns()


