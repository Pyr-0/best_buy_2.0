import products
import store

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
			products = best_buy.get_all_products()
			print("----------")
			for index, product in enumerate(products, 1):
				print(f"{index}. {product.show()}")
			print("---------- \n")
		elif choice == "2":
			print(f"Total of {best_buy.get_total_quantity()} items in store")
		elif choice == "3":
			shopping_list = []
			products = best_buy.get_all_products()
			print("----------")
			for index, product in enumerate(products, 1):
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
						print("Invalid choice. Please enter a number between 1-3.")
						continue
					selected_product = products[product_num - 1]
					amount = int(input("What amount do you want? "))
					if not amount:
						print("No amount entered. Returning to menu.")
						break
					ammount = int(amount)
					if amount <= 0:
						print("Quantity must be greater than 0.")
					if amount > selected_product.get_quantity():
						print(f"Not enough stock available. Max available: {selected_product.get_quantity()}")
						continue
					shopping_list.append((selected_product, amount))
					print("Product added to list!")
				except (IndexError, ValueError):
					print("Invalid selection. Try again.")
			if shopping_list:
				try:
					print(f"Total order cost: {best_buy.order(shopping_list)} dollars.")
				except ValueError:
					print("Error while making order! Quantity larger than what exists.")
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
	product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
					products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
					products.Product("Google Pixel 7", price=500, quantity=250)]
	best_buy = store.Store(product_list)
	main(best_buy)
