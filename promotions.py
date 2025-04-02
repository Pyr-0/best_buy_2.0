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
    """Applies a percentage discount to a product."""
    def __init__(self, name, percent):
        super().__init__(name)
        if not 0 <= percent <= 100:
            raise ValueError("Percent discount must be between 0 and 100")
        self.percent = percent
        
    def apply_promotion(self, product, quantity):
        """Apply a percentage discount to the total price."""
        original_price = product.price * quantity
        discount = original_price * (self.percent / 100)
        return original_price - discount


class SecondHalfPrice(Promotion):
    """Every second item costs half price."""
    def apply_promotion(self, product, quantity):
        """Apply second item at half price promotion."""
        # Calculate how many full-price and half-price items
        full_price_count = (quantity + 1) // 2  # Ceiling division for odd quantities
        half_price_count = quantity // 2        # Floor division
        
        # Calculate total price
        total = (full_price_count * product.price) + (half_price_count * product.price * 0.5)
        return total


class ThirdOneFree(Promotion):
    """Buy 2, get 1 free promotion."""
    def apply_promotion(self, product, quantity):
        """Apply buy 2, get 1 free promotion."""
        # Calculate how many free items
        free_items = quantity // 3
        
        # Calculate paid items
        paid_items = quantity - free_items
        
        # Calculate total price
        total = paid_items * product.price
        return total 