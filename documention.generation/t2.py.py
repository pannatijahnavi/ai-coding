"""Problem 2: Documentation styles for a login helper.

Critical comparison for a college lab record
---------------------------------------------

1. Docstring format
   Advantages: A docstring stays with the function and can be read using
   help(). It gives developers a quick explanation of the function's purpose.
   Disadvantages: A short docstring may leave out details about parameters or
   the return value.
   Suitable use: Small functions where a short explanation is enough.

2. Inline comment format
   Advantages: A comment explains a particular line next to the code. It can
   make a simple comparison or calculation easier to follow.
   Disadvantages: Comments are not shown by help(), can make short code look
   crowded, and may become incorrect if the code changes.
   Suitable use: Non-obvious steps or decisions inside a function.

3. Google-style documentation format
   Advantages: It consistently describes the purpose, arguments, and return
   value. This makes it easy for new developers to scan and understand.
   Disadvantages: It requires more writing and can be excessive for a tiny
   private function.
   Suitable use: Shared functions in team projects and public libraries.

Recommendation
--------------
Google-style documentation is the most helpful choice for new developers
onboarding to a project. Its headings give readers the same information in the
same order for every function. This reduces guesswork and helps developers
understand how to call the function quickly. A short inline comment can still
be used for an unusual implementation detail, but it should not replace the
main docstring.
"""


def login_docstring(user, password, credentials):
	"""Return whether the supplied password matches the user's credential."""
	return credentials.get(user) == password


def login_comments(user, password, credentials):
	# Look up the stored credential for this user.
	stored_password = credentials.get(user)
	# The login succeeds only when the stored value matches the supplied one.
	return stored_password == password


def login_google(user, password, credentials):
	"""Check whether a user's supplied password matches their credential.

	Args:
		user (str): The username to look up.
		password (str): The password supplied by the user.
		credentials (dict): A mapping of usernames to stored credentials.

	Returns:
		bool: True when the stored credential equals ``password``; otherwise,
		False.
	"""
	return credentials.get(user) == password


if __name__ == "__main__":
	sample_credentials = {"student": "lab123"}
	print("Docstring version:", login_docstring("student", "lab123", sample_credentials))
	print("Inline-comment version:", login_comments("student", "wrong", sample_credentials))
	print("Google-style version:", login_google("student", "lab123", sample_credentials))
