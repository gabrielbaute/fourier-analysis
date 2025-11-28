import logging
from app.signal_procesor import Signal

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(name)s]:[%(levelname)s]: %(message)s')

if __name__ == "__main__":
    signal = Signal(port="COM15")
    signal.stream()
