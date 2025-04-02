import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_non_stocked_product_creation():
    """Test that creating a non-stocked product works correctly."""
    # Create a non-stocked product
    product = NonStockedProduct("Windows License", price=125)
    
    # Check that quantity is 0 but product is active
    assert product.get_quantity() == 0
    assert product.is_active() == True
    
def test_non_stocked_product_buying():
    """Test that buying a non-stocked product works."""
    # Create a non-stocked product
    product = NonStockedProduct("Windows License", price=125)
    
    # Buy multiple products
    total = product.buy(3)
    
    # Check total price
    assert total == 375  # 3 * 125 = 375
    
    # Check that quantity is still 0 and product is still active
    assert product.get_quantity() == 0
    assert product.is_active() == True

def test_limited_product_creation():
    """Test that creating a limited product works correctly."""
    # Create a limited product with maximum 1 per order
    product = LimitedProduct("Shipping", price=10, quantity=100, maximum=1)
    
    # Check that product attributes are set correctly
    assert product.maximum == 1
    assert product.get_quantity() == 100
    assert product.is_active() == True

def test_limited_product_buying_within_limit():
    """Test that buying a limited product within the limit works."""
    # Create a limited product with maximum 2 per order
    product = LimitedProduct("Shipping", price=10, quantity=100, maximum=2)
    
    # Buy within the limit
    total = product.buy(2)
    
    # Check total price and updated quantity
    assert total == 20  # 2 * 10 = 20
    assert product.get_quantity() == 98

def test_limited_product_buying_exceeds_limit():
    """Test that buying a limited product exceeding the limit raises an exception."""
    # Create a limited product with maximum 2 per order
    product = LimitedProduct("Shipping", price=10, quantity=100, maximum=2)
    
    # Try to buy more than the maximum limit
    with pytest.raises(ValueError):
        product.buy(3) 