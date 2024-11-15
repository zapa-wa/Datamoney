# src/main.py
import yaml
import logging.config
import os
from client import ExchangeClient
from service import Service


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def setup_logging(log_file, log_level):
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=getattr(logging, log_level.upper(), "INFO"),  # Usa "INFO" si el nivel es incorrecto
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, mode='a')  # 'a' para agregar al archivo existente
        ]
    )
    print(f"Logging configurado en el archivo: {log_file}")

def main():
    print("Welcome to Data Money!")
    print("The program where you can check your currency exchange ")
    # Load configuration
    config = load_config()

    # Set up logging
    setup_logging(config['log_file'], config['log_level'])

    # Initialize client and service
    exchange_client = ExchangeClient(config)
    service = Service()

    # Fetch exchange rate and convert currency
    rate = exchange_client.get_exchange_rate()
    converted_amount = service.convert_currency(exchange_client.amount, rate)

    if converted_amount is not None:
        print(
            f"{exchange_client.amount} {exchange_client.from_currency} is equal to {converted_amount:.2f} {exchange_client.to_currency}")


if __name__ == "__main__":
    main()
