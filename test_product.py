import pytest
from product import product_details


def test_product_details_basic():
    """Test product details with basic sample data"""
    product_id = "1598534756"
    name = "iphone 17"
    quantity = 1
    price = 80000
    
    expected_output = (
        "Product ID: 1598534756\n"
        "Product Name: iphone 17\n"
        "Quantity: 1\n"
        "Price: 80000"
    )
    
    result = product_details(product_id, name, quantity, price)
    assert result == expected_output
