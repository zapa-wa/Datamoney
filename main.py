# src/main.py
import yaml
import logging.config
import os
from client import ExchangeClient
from service import Service


def load_config():
    with open(os.path.join(os.path.dirname(__file__), "../config/config.yaml"), "r") as file:
        return yaml.safe_load(file)


def setup_logging(log_file, log_level):
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def main():
    # Load configuration
    config = load_config()

    # Set up logging
    setup_logging(config['log_file'], config['log_level'])

    # Initialize client and service
    exchange_client = ExchangeClient(config)
    service = Service()

    # Fetch exchange rate and convert currency
    rate = exchange_client.get_exchange_rate()
    converted_amount = service.convert_currency(config['amount'], rate)

    if converted_amount is not None:
        print(
            f"{config['amount']} {config['base_currency']} is equal to {converted_amount:.2f} {config['target_currency']}")


if __name__ == "__main__":
    main()
