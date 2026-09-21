def is_strong_password(password):
	"""Return True when password meets all strength requirements."""
	# Check the password length and reject passwords containing spaces.
	if len(password) < 8 or " " in password:
		return False

	# Check that the password contains each required character type.
	has_uppercase = any(character.isupper() for character in password)
	has_lowercase = any(character.islower() for character in password)
	has_digit = any(character.isdigit() for character in password)
	has_special = any(not character.isalnum() for character in password)

	return has_uppercase and has_lowercase and has_digit and has_special


# Tests are written before the function is used, following TDD.
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("ABCD@1234") == False

# Edge-case tests: spaces are not allowed, and the minimum length can pass.
assert is_strong_password("Abc 123@") == False
assert is_strong_password("Abcde@12") == True

print("All Task 1 tests passed!")
