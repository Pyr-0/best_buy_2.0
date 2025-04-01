import pytest
from products import Product

def test_create_normal_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() == True

def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    # Empty name
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    
    # Negative price
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)
    
    # Negative quantity
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-5)

def test_product_becomes_inactive_at_zero_quantity():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    assert product.is_active() == True
    
    # Set quantity to zero
    product.set_quantity(0)
    assert product.is_active() == False

def test_product_purchase_modifies_quantity():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = Product("MacBook Air M2", price=1450, quantity=10)
    initial_quantity = product.get_quantity()
    
    # Buy 3 items
    purchase_amount = 3
    total_price = product.buy(purchase_amount)
    
    # Check quantity decreased
    assert product.get_quantity() == initial_quantity - purchase_amount
    # Check correct price returned
    assert total_price == product.price * purchase_amount

def test_buying_larger_quantity_than_exists():
    """Test that buying a larger quantity than exists invokes exception."""
    product = Product("MacBook Air M2", price=1450, quantity=2)
    
    # Try to buy more than available
    with pytest.raises(ValueError):
        product.buy(3) 