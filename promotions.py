from abc import ABC, abstractmethod

class Promotion(ABC):
	"""Abstract base class for product promotions."""
	def __init__(self, name):
		self.name = name

	@abstractmethod
	def apply_promotion(self, product, quantity):
		"""Apply promotion to a product purchase."""
		pass

class PercentDiscount(Promotion):
	def __init__(self, name: str, percent: float):
		super().__init__(name)
		self.percent = percent

def apply_promotion(self, product, quantity) -> float:
	"""Applies a percentage discount to the total price."""
	discount = (self.percent / 100) * (product.price * quantity)
	return (product.price * quantity) - discount

class SecondHalfPrice(Promotion):
	def apply_promotion(self, product, quantity) -> float:
		"""Applies a second item at half price discount."""
		full_price_items = quantity // 2 + quantity % 2  # Every second item is half price
		half_price_items = quantity // 2
		return (full_price_items * product.price) + (half_price_items * product.price * 0.5)
	
class ThirdOneFree(Promotion):
	def apply_promotion(self, product, quantity) -> float:
		"""Applies 'Buy 2, Get 1 Free' discount."""
		payable_items = quantity - (quantity // 3)  # Every third item is free
		return payable_items * product.price