import sys

raw_product_name = (
	" ".join(sys.argv[1:])
	if len(sys.argv) > 1
	else input("What's the product name? ")
)
product_name = raw_product_name.strip().lower()

match product_name:
	case "electronics" | "gadget":
		category = "High Margin"
	case _ if product_name.startswith("tech"):
		category = "High Margin"
	case "clothing" | "apparel":
		category = "Medium Margin"
	case "food" | "grocery":
		category = "Low Margin"
	case _:
		category = "Uncategorized - Review Needed"

print(f"Product: {product_name} | Category: {category}")
