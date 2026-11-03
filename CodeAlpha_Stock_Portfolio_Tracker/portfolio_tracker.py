import csv
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
}
def get_portfolio():
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Type 'done' when you are finished.\n")
    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Please choose from the available stocks.")
            continue
        try:
            quantity = int(input(f"Quantity of {symbol}: "))
        except ValueError:
            print("Quantity must be a whole number.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} x {symbol}\n")
    return portfolio
def calculate_investment(portfolio):
    rows = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        rows.append({"symbol": symbol, "quantity": quantity,
                     "price": price, "value": value})
        total += value
    return rows, total
def display_portfolio(rows, total):
    print("\n{:<8}{:>10}{:>12}{:>14}".format("Stock", "Quantity", "Price", "Value"))
    print("-" * 44)
    for row in rows:
        print("{:<8}{:>10}{:>12}{:>14}".format(
            row["symbol"], row["quantity"],
            f"${row['price']}", f"${row['value']}"))
    print("-" * 44)
    print(f"Total investment value: ${total}")
def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["symbol", "quantity", "price", "value"])
        writer.writeheader()
        writer.writerows(rows)
        writer.writerow({"symbol": "TOTAL", "quantity": "", "price": "", "value": total})
    print(f"Portfolio saved to {filename}")
def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    rows, total = calculate_investment(portfolio)
    display_portfolio(rows, total)
    if input("\nSave result to CSV? (y/n): ").strip().lower() == "y":
        save_to_csv(rows, total)
if __name__ == "__main__":
    main()
