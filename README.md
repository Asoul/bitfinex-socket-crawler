# Bitfinex Websocket Crawler

A Bitfinex websocket (v1.1) crawler, save ticker data to MySQL, run with supervisor.

<p align="center">
  <img src="https://raw.githubusercontent.com/Asoul/bitfinex-socket-crawler/master/img/bitfinex.jpg"></img>
</p>

## Requirements

- Python3
- MySQL
- virtualenv (install via pip)

## Installation

```
# Create virtual environment
virtualenv -p `which python3` venv

# Use virtual environment
. venv/bin/activate

# Install packages
pip install -r requirements.txt

# Build database (assume user is root without password)
mysql -u root -e "CREATE DATABASE bitfinex"

# (Optional) Change database url in alembic.ini and server.py for your customize database
vim alembic.ini
vim server.py

# Build tables
alembic upgrade head
```

## Execute

```
python server.py
```

## Execute via supervisor (Run in background on your server)

```
# Install supervisor
sudo apt-get install -y supervisor

# Change supervisor paths
sudo vim supervisor/bitfinex-socket-crawler.conf

# Add script for supervisor
sudo cp ./supervisor/bitfinex-socket-crawler.conf /etc/supervisor/conf.d/

# Load script
sudo supervisorctl reread
sudo supervisorctl update

# Execute supervisor
sudo supervisorctl start bitfinex-socket-crawler
```

# Contribution

Any issues or PRs are very welcome, or contact with me `azx754@gmail.com`.

# License

MIT

# Donation

BTC Wallet: `3QB4Liv4Yp1ttpHnk8DT135juhKTBEWDc7`

<p align="center">
  <img src="https://raw.githubusercontent.com/Asoul/bitfinex-socket-crawler/master/img/qrcode.png"></img>
</p>
