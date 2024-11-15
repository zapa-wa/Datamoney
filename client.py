
import requests
import logging

class ExchangeClient:
    def __init__(self, config):
        self.api_url = config['api_url']
        self.base_currency = config['base_currency']
        self.target_currency = config['target_currency']
        self.amount = config['amount']
        self.logger = logging.getLogger("ExchangeClient")

    def get_exchange_rate(self):
        params = {
            "base": self.base_currency,
            "symbols": self.target_currency
        }
        try:
            self.logger.info("Fetching exchange rate...")
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()
            rate = data['rates'][self.target_currency]
            self.logger.info(f"Exchange rate fetched successfully: {rate}")
            return rate
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch exchange rate: {e}")
            return None
