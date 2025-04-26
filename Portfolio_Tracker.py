import yfinance as yf
portfolio= {}

#add a stock

def add_stock(ticker, shares):
    if ticker in portfolio:
        portfolio[ticker]+=shares 
    else:
        portfolio[ticker]=shares
    print(f"Added {shares} shares of {ticker}")
    
    #Remove a stock
    
def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker] 
        print(f"Removed {ticker} from portfolio.")
    else:
        print("Stock not found in portfolio.")
        
    #Show the portfolio
    
def show_portfolio():
    total_value=0
    print("\n Your Portfolio:\n")
    for ticker ,shares in portfolio.items():
        stock = yf.Ticker(ticker)
        price = stock.info['regularMarketPrice']
        value = shares*price 
        total_value += value
        print(f"{ticker.upper()}:{shares} shares x ${price:.2f} = ${value:.2f}")
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    
    #Menu for user Input
    
def menu():
    while True:
        print("\n--- Stock Portfolio Tracker----")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        
        choice = input ("Choose an option (1-4): ")
        if choice == "1":
            ticker =input("Enter stock ticker (e.g , AAPL): ").upper()
            shares = int (input("Enter number of shares:"))
            add_stock(ticker, shares)
        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    menu()
    
