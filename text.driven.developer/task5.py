from datetime import datetime


def validate_and_format_date(date_str):
	"""Validate an MM/DD/YYYY date and return it as YYYY-MM-DD."""
	try:
		# Parse the date and let datetime check months, days, and leap years.
		date = datetime.strptime(date_str, "%m/%d/%Y")

		# Make sure the input used the required two-digit format.
		if date.strftime("%m/%d/%Y") != date_str:
			return "Invalid Date"

		return date.strftime("%Y-%m-%d")
	except (TypeError, ValueError):
		# TypeError handles non-string input; ValueError handles bad dates.
		return "Invalid Date"


# Tests written for the date validation function.
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"

# Edge-case tests: leap year, invalid month/day, and incorrect format.
assert validate_and_format_date("02/29/2024") == "2024-02-29"
assert validate_and_format_date("13/01/2023") == "Invalid Date"
assert validate_and_format_date("04/31/2023") == "Invalid Date"
assert validate_and_format_date("2023-10-15") == "Invalid Date"

print("All Task 5 tests passed!")
