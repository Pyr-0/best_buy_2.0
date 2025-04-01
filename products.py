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

class NonStockedProduct(Product):
	"""Represents a non-physical product that doesn't have stock."""
	def __init__(self, name:str, price:float):
		"""Initialize a non-stocked product with quantity fixed at 0."""
		super().__init__(name, price, quantity=0)
		self.active = True

	def show(self):
		"""Returns a string representation of the non-stocked product."""
		return f"{self.name}, Price: {self.price}, Non-stocked product"

	def buy(self, quantity):
		"""Buy a non-stocked product (no quantity tracking)."""
		return self.price * quantity

class LimitedProduct(Product):
	"""Represents a product that can only be purchased in limited quantity per order."""
	def __init__(self, name:str, price:float, quantity:int, maximum:int):
		"""Initialize a limited product with a maximum purchase quantity."""
		super().__init__(name, price, quantity)
		self.maximum = maximum
		
	def show(self):
		"""Returns a string representation of the limited product."""
		return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
		
	def buy(self, quantity):
		"""Buy a limited product with quantity restrictions."""
		if quantity > self.maximum:
			raise ValueError(f"Cannot buy more than {self.maximum} units in a single order")
			
		return super().buy(quantity)
