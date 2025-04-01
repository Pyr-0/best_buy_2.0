class Store:
	""" Represents a store containing multiple products."""
	def __init__(self, products):
		""" Initializes the store with a list of products."""
		self.products = products

	def add_product(self, product):
		""" Adds a product to the store."""
		self.products.append(product)

	def remove_product(self, product):
		""" Removes a product from the store."""
		self.products.remove(product)

	def get_total_quantity(self):
		"""Returns the total quantity of all products in the store."""
		return sum(product.get_quantity() for product in self.products)

	def get_all_products(self):
		"""Returns a list of active products in the store."""
		return [product for product in self.products if product.is_active()]

	def order(self, shopping_list):
		""" Processes an order containing multiple products."""
		total_price = 0
		for product, quantity in shopping_list:
			total_price += product.buy(quantity)
		return total_price