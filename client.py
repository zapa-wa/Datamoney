
import requests
import logging

class ExchangeClient:
    def __init__(self, config):
        self.api_url = config['api_url']
        self.from_currency = input("from Currency: ")
        self.to_currency = input(" to Currency: ")
        self.amount = float(input("amount: "))
        self.logger = logging.getLogger("ExchangeClient")
        self.prove_currency = config['prove_currency']

    def get_exchange_rate(self):
        try:
            self.logger.info("Fetching exchange rate...")
            response = requests.get(self.api_url)
            data = response.json()
            if response.status_code != 200:
                print("Error in exchange rate")
                return None
            # Verificar si 'conversion_rates' y la moneda objetivo están en la respuesta
            if "conversion_rates" in data and self.to_currency in data["conversion_rates"]:
                if self.from_currency == "USD":
                    rate = data["conversion_rates"][self.to_currency]
                    self.logger.info(f"Exchange rate fetched successfully: {rate}")
                    return rate
                elif self.from_currency != "USD":
                    self.prove_currency = "USD"
                    previous_rate_1 = data["conversion_rates"][self.from_currency]
                    previous_rate_2 = data["conversion_rates"][self.to_currency]
                    rate = previous_rate_2 / previous_rate_1
                    self.logger.info(f"Exchange rate fetched successfully: {rate}")
                    return rate
            else:
                self.logger.error("La respuesta de la API no contiene 'rates' o la moneda objetivo.")
                return None
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch exchange rate: {e}")
            return None
