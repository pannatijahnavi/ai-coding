"""Problem 1: Documentation styles for a simple mathematical utility.

Comparison for a college lab record
------------------------------------

1. Python docstrings
   Advantages: They are stored with the function, can be viewed with help(),
   and explain the purpose of the function to users and maintainers.
   Disadvantages: A short docstring may not describe every implementation
   detail, and a long one can become difficult to read.
   Suitable use: Public functions, classes, and modules that other people use.

2. Inline comments
   Advantages: They explain a particular line or step directly beside the
   code and are useful for explaining non-obvious logic.
   Disadvantages: They are not available through help(), can make code noisy,
   and may become incorrect when the code changes.
   Suitable use: Complex algorithms, unusual decisions, or important edge
   cases that are not obvious from the code itself.

3. Google-style documentation
   Advantages: It gives docstrings a consistent structure for descriptions,
   arguments, return values, and errors. Documentation tools can also process
   this format easily.
   Disadvantages: It takes more time to write and is unnecessarily detailed
   for very small private functions.
   Suitable use: Public libraries and larger projects with several developers.

Recommendation
--------------
Google-style documentation is the most effective choice for a mathematical
utilities library. Mathematical utilities are often reused by other programs,
so users need consistent information about inputs, outputs, and errors. A
Google-style docstring provides this information while remaining readable for
beginners. Inline comments should still be added only where an algorithm is
not self-explanatory.
"""


def find_max_docstring(numbers):
	"""Return the largest value in a non-empty collection of numbers."""
	return max(numbers)


def find_max_comments(numbers):
	# Python's built-in max() compares the values and returns the largest one.
	# The input must contain at least one value.
	return max(numbers)


def find_max_google(numbers):
	"""Find and return the maximum number from an iterable.

	Args:
		numbers (iterable): A non-empty iterable of comparable numbers.

	Returns:
		number: The greatest value in ``numbers``.

	Raises:
		ValueError: If ``numbers`` is empty.
	"""
	return max(numbers)


if __name__ == "__main__":
	sample_numbers = [12, 4, 27, 9]
	print("Docstring version:", find_max_docstring(sample_numbers))
	print("Inline-comment version:", find_max_comments(sample_numbers))
	print("Google-style version:", find_max_google(sample_numbers))
