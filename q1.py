revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))

profit = revenue - cost

if revenue > 0:
    margin = (profit / revenue) * 100
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")
