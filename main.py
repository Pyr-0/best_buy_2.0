import products
import store
import promotions

def main(best_buy):
	"""Starts the store user interface."""
	while True:
		print("\n   Store Menu\n   ----------")
		print("1. List all products in store")
		print("2. Show total amount in store")
		print("3. Make an order")
		print("4. Quit")
		choice = input("Please choose a number: ")

		if choice == "1":
			products_list = best_buy.get_all_products()
			print("----------")
			for index, product in enumerate(products_list, 1):
				print(f"{index}. {product.show()}")
			print("---------- \n")
		elif choice == "2":
			print(f"Total of {best_buy.get_total_quantity()} items in store")
		elif choice == "3":
			shopping_list = []
			products_list = best_buy.get_all_products()
			print("----------")
			for index, product in enumerate(products_list, 1):
				print(f"{index}. {product.show()}")
			print("---------- \n")
			while True:
				print("\n(Press Enter without a number to return to the menu)")
				product_num = input("Which product # do you want? ")
				if not product_num:
					break
				try:
					product_num = int(product_num)
					if product_num <= 0:
						print("Invalid choice. Please enter a valid product number.")
						continue
					selected_product = products_list[product_num - 1]
					amount = int(input("What amount do you want? "))
					if not amount:
						print("No amount entered. Returning to menu.")
						break
					if amount <= 0:
						print("Quantity must be greater than 0.")
						continue
					
					try:
						# Check if we have enough stock or if it's a special product
						if isinstance(selected_product, products.NonStockedProduct):
							# Non-stocked products can be purchased in any quantity
							pass
						elif isinstance(selected_product, products.LimitedProduct):
							# Limited products have a maximum per order
							if amount > selected_product.maximum:
								print(f"Cannot buy more than {selected_product.maximum} of this item in a single order.")
								continue
							if amount > selected_product.get_quantity():
								print(f"Not enough stock available. Max available: {selected_product.get_quantity()}")
								continue
							# Check if this limited product is already in the shopping list
							if any(item[0] == selected_product for item in shopping_list):
								print("This limited product can only be added once to the order.")
								continue
						else:
							# Regular products check quantity
							if amount > selected_product.get_quantity():
								print(f"Not enough stock available. Max available: {selected_product.get_quantity()}")
								continue
						
						shopping_list.append((selected_product, amount))
						print("Product added to list!")
					except ValueError as e:
						print(f"Error: {e}")
				except (IndexError, ValueError):
					print("Invalid selection. Try again.")
			
			if shopping_list:
				try:
					total = best_buy.order(shopping_list)
					print(f"Total order cost: ${total:.2f}")
				except ValueError as e:
					print(f"Error while making order! {e}")
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
	# setup initial stock of inventory
	product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
				   products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
				   products.Product("Google Pixel 7", price=500, quantity=250),
				   products.NonStockedProduct("Windows License", price=125),
				   products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
				  ]

	# Create promotion catalog
	second_half_price = promotions.SecondHalfPrice("Second Half price!")
	third_one_free = promotions.ThirdOneFree("Third One Free!")
	thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

	# Add promotions to products
	product_list[0].set_promotion(second_half_price)
	product_list[1].set_promotion(third_one_free)
	product_list[3].set_promotion(thirty_percent)
	
	best_buy = store.Store(product_list)
	main(best_buy)
