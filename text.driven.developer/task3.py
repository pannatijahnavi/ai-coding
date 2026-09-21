def is_anagram(str1, str2):
	"""Return True when two strings contain the same letters or digits."""
	# Keep only letters and digits, and make all characters lowercase.
	cleaned_str1 = ""
	cleaned_str2 = ""

	for character in str1:
		if character.isalnum():
			cleaned_str1 += character.lower()

	for character in str2:
		if character.isalnum():
			cleaned_str2 += character.lower()

	# Anagrams have the same characters when sorted.
	return sorted(cleaned_str1) == sorted(cleaned_str2)


# Tests written for the function, including the requested edge cases.
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty Room") == True
assert is_anagram("", "") == True
assert is_anagram("python", "python") == True
assert is_anagram("A gentleman!", "Elegant man") == True

print("All Task 3 tests passed!")
