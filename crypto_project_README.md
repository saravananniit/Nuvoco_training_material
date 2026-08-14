Crypto_Project_demo:

uv add requests
================================================================
crypto_monitor/monitor.py

import requests
import time

class Monitor:
    def __init__(self, sensor, interval=15):
        self.sensor = sensor
        self.interval = interval

    def start(self):
        print(f"\nMonitoring {self.sensor.name} every {self.interval}s... (Ctrl+C to stop)\n")
        try:
            while True:
                try:
                    price = self.sensor.read()
                    print(f"[{self.sensor.name}] {price} {self.sensor.currency.upper()}")
                except RuntimeError as e:
                    print(f"{e}")
                except requests.exceptions.RequestException as e:
                    print(f"Network error: {e}")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\nStopped.")

============================================================
crypto_monitor/sensor.py

import requests

class Sensor:
    def __init__(self, name):
        self.name = name

    def read(self):
        raise NotImplementedError

class BitcoinPriceSensor(Sensor):
    def __init__(self, currency):
        super().__init__("Bitcoin Price")
        self.currency = currency

    def read(self):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={self.currency}"
        response = requests.get(url, timeout=5)

        if response.status_code == 429:
            raise RuntimeError("Rate limited by API. Waiting before retry...")

        response.raise_for_status()
        return response.json()["bitcoin"][self.currency]


==============================================================
crypto_monitor/__init__.py:

from .sensor import BitcoinPriceSensor
from .monitor import Monitor

===========================================================
main.py

import requests
from crypto_monitor import BitcoinPriceSensor, Monitor

def get_valid_currencies():
    url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return set(response.json())

def get_currency_input(valid_currencies):
    while True:
        currency = input("Enter currency (e.g. usd, inr, eur): ").strip().lower()
        if currency in valid_currencies:
            return currency
        print(f"'{currency}' is not valid. Try again.\n")

def main():
    valid_currencies = get_valid_currencies()
    currency = get_currency_input(valid_currencies)

    sensor = BitcoinPriceSensor(currency)
    Monitor(sensor, interval=15).start()  # 15s is safer for free tier

if __name__ == "__main__":
    main()
=====================================================

Flow:

User
  |
  v
main.py
  |
  +--> CoinGecko API (Get supported currencies)
  |
  +--> User selects currency
  |
  v
BitcoinPriceSensor
  |
  v
Monitor
  |
  +--> Every 15 seconds
          |
          v
      Sensor reads data
          |
          v
      CoinGecko API
          |
          v
      Bitcoin Price
          |
          v
      Display on Screen

=================================================================

      