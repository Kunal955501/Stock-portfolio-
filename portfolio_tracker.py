# Predefined stock prices (hardcoded dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker!\n")
print("Available Stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' when you are finished.\n")

# Input from user
while True:
    stock = input("Enter stock symbol (AAPL/TSLA/etc): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❗ Invalid stock symbol. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("❗ Please enter a valid positive number for quantity.\n")
        continue

    # Add to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

print("\n📊 Your Portfolio Summary:")
total_value = 0

for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares x ₹{stock_prices[stock]} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")

# Optional: Save to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        file.write(f"{stock}: {qty} x ₹{stock_prices[stock]} = ₹{value}\n")
    file.write(f"\nTotal Investment: ₹{total_value}\n")

print("\n✅ Summary saved to 'portfolio_summary.txt'")
