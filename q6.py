def is_profitable(revenue: float, cost: float) -> bool:
	return revenue > cost


def main() -> None:
	try:
		revenue = float(input("Business revenue: $"))
		cost = float(input("Business cost: $"))
	except ValueError:
		print("Please enter revenue and cost as numbers.")
		return

	if revenue < 0 or cost < 0:
		print("Revenue and cost cannot be negative.")
		return

	category = input("Business category (High Margin, Medium Margin, Low Margin): ")
	profit = revenue - cost

	if is_profitable(revenue, cost):
		print(f"Profit: ${profit:,.2f}")
		match category.strip().lower():
			case "high margin" | "high":
				suggestion = "Reinvest in growth."
			case "medium margin" | "medium":
				suggestion = "Test a focused improvement before scaling."
			case "low margin" | "low":
				suggestion = "Prioritize cost control before expanding."
			case _:
				suggestion = "Review the category before committing funds."
		print(f"Investment suggestion: {suggestion}")
	elif profit == 0:
		print("Break-even: $0.00. Hold investment until returns improve.")
	else:
		print(f"Operating loss: ${-profit:,.2f}. Review costs before investing.")


if __name__ == "__main__":
	main()
