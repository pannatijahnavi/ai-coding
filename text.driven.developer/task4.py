class Inventory:
	def __init__(self):
		# Store each item name and its quantity in a dictionary.
		self.items = {}

	def add_item(self, name, quantity):
		# Add to the current quantity, or start at zero for a new item.
		self.items[name] = self.items.get(name, 0) + quantity

	def remove_item(self, name, quantity):
		# Reduce the quantity without allowing the stock to become negative.
		current_quantity = self.items.get(name, 0)
		self.items[name] = max(current_quantity - quantity, 0)

	def get_stock(self, name):
		# Return zero when the item is not in the inventory.
		return self.items.get(name, 0)


# Tests written for the Inventory class.
inv = Inventory()

inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3

# Edge-case tests: adding an existing item, a missing item, and over-removal.
inv.add_item("Pen", 2)
assert inv.get_stock("Pen") == 7

assert inv.get_stock("Pencil") == 0

inv.remove_item("Book", 10)
assert inv.get_stock("Book") == 0

print("All Task 4 tests passed!")
