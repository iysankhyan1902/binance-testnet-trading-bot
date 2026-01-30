import argparse
from bot.orders import OrderService
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

logger = setup_logger("trading_bot", "logs/trading.log")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
        service = OrderService()

        print("\nOrder Request:")
        print(vars(args))

        if args.type == "MARKET":
            response = service.place_market_order(
                args.symbol, args.side, args.quantity
            )
        else:
            response = service.place_limit_order(
                args.symbol, args.side, args.quantity, args.price
            )

        print("\nOrder Response:")
        print(response)

        logger.info(f"ORDER SUCCESS: {response}")
        print("\n✅ Order placed successfully")

    except Exception as e:
        logger.error(f"ORDER FAILED: {str(e)}")
        print("\n❌ Order failed:", str(e))

if __name__ == "__main__":
    main()
