import ccxt
import time

def arbitrage(pair, threshold):
    # Create exchange instances
    exchange_A = ccxt.binance() # replace with your desired exchanges
    exchange_B = ccxt.kraken()

    while True:
        # Get ticker info from both exchanges
        ticker_A = exchange_A.fetch_ticker(pair)
        ticker_B = exchange_B.fetch_ticker(pair)

        # Extract bid and ask prices
        bid_A, ask_A = ticker_A['bid'], ticker_A['ask']
        bid_B, ask_B = ticker_B['bid'], ticker_B['ask']

        # Check if any price is None before proceeding
        if all([bid_A, ask_A, bid_B, ask_B]):
            if ask_A < bid_B:
                difference = bid_B - ask_A
                if difference > threshold:
                    print(f"Arbitrage opportunity detected! Buy on Exchange A at {ask_A} and sell on Exchange B at {bid_B} for a profit of {difference}.")

            if ask_B < bid_A:
                difference = bid_A - ask_B
                if difference > threshold:
                    print(f"Arbitrage opportunity detected! Buy on Exchange B at {ask_B} and sell on Exchange A at {bid_A} for a profit of {difference}.")

        time.sleep(1)  # Sleep for 1 second to avoid hitting rate limits. Adjust based on the rate limits of the exchanges' APIs.

arbitrage('BTC/USDT', 10)
