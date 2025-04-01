class Product:
	"""Represents a product with a name, price, quantity, and active status."""
	def __init__(self, name:str, price:float, quantity:int):
		"""Initializes a new product instance and raises ValueError if invalid."""
		if not name or price < 0 or quantity < 0:
			raise ValueError("Invalid product attributes")
		self.name = name
		self.price = price
		self.quantity = quantity
		self.active = True

	def get_quantity(self):
		"""Returns the current quantity of the product."""
		return self.quantity

	def set_quantity(self, quantity):
		"""Sets the product's quantity and deactivates it if quantity reaches zero."""
		self.quantity = quantity
		if self.quantity == 0:
			self.deactivate()

	def is_active(self):
		"""Returns whether the product is active."""
		return self.active

	def activate(self):
		"""Activates the product."""
		self.active = True

	def deactivate(self):
		"""Deactivates the product."""
		self.active = False

	def show(self):
		"""Returns a string representation of the product."""
		return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

	def buy(self, quantity):
		""" Buys a given quantity of the product, updating stock."""
		if quantity > self.quantity:
			raise ValueError("Not enough stock available")
		self.quantity -= quantity
		if self.quantity == 0:
			self.deactivate()
		return self.price * quantity
