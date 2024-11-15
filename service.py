
import logging

class Service:
    def __init__(self):
        self.logger = logging.getLogger("Service")

    def convert_currency(self, amount, rate):
        if rate:
            converted_amount = amount * rate
            self.logger.info(f"Converted amount: {converted_amount:.2f}")
            return converted_amount
        else:
            self.logger.warning("Invalid exchange rate provided.")
            return None
