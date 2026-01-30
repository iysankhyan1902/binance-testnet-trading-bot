import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceTestnetClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        secret_key = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not secret_key:
            raise Exception("API keys not found")

        self.client = Client(api_key, secret_key)

       
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        server_time = self.client.futures_time()["serverTime"]
        local_time = int(time.time() * 1000)

        self.client.timestamp_offset = server_time - local_time
        self.client.RECV_WINDOW = 10000  

    def get_client(self):
        return self.client
