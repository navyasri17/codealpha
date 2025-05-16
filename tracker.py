import yfinance as yf

portfolio = {}

def add_stock(symbol, shares):
    portfolio[symbol] = portfolio.get(symbol, 0) + shares

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]

def display_portfolio():
    print("\n📈 Your Portfolio:")
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]
        total = shares * price
        print(f"{symbol}: {shares} shares @ ${price:.2f} each → Total: ${total:.2f}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Show Portfolio\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            sym = input("Stock symbol (e.g., AAPL): ").upper()
            sh = int(input("Number of shares: "))
            add_stock(sym, sh)
        elif choice == '2':
            sym = input("Stock symbol to remove: ").upper()
            remove_stock(sym)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
