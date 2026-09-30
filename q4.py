def get_tax_bracket(income: float) -> str:
	if income < 0:
		return "Invalid income."
	elif income < 50000:
		return "Low (10%)"
	elif income < 100000:
		return "Medium (20%)"
	else:
		return "High (30%)"


if __name__ == "__main__":
	income = float(input("What's your annual income? "))
	bracket = get_tax_bracket(income)

	if income < 50000:
		rate = 0.10
	elif income < 100000:
		rate = 0.20
	else:
		rate = 0.30

	estimated_tax = income * rate if income >= 0 else 0.0
	print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}.")
