def format_greeting(name: str, title: str = "Customer") -> str:
	cleaned_name = name.strip().lower().title()
	if not cleaned_name:
		return "Hello, Valued Customer!"

	first_name = cleaned_name.split()[0]
	return f"Hello, {first_name} ({title})!"


if __name__ == "__main__":
	full_name = input("What's your full name?")
	print(format_greeting(full_name))
