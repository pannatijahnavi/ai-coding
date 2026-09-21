def classify_number(n):
	"""Return the classification of a number."""
	# Strings, None, and other non-number values are invalid inputs.
	if not isinstance(n, (int, float)):
		return "Invalid"

	# Check each possible classification using a loop.
	classifications = [
		(n > 0, "Positive"),
		(n < 0, "Negative"),
		(n == 0, "Zero"),
	]

	for condition, result in classifications:
		if condition:
			return result

	return "Invalid"


# Tests written for the function, including boundary and invalid values.
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number(1) == "Positive"
assert classify_number(-1) == "Negative"
assert classify_number("10") == "Invalid"
assert classify_number(None) == "Invalid"

print("All Task 2 tests passed!")
