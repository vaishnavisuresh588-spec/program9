def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ${price}"
    )
    return result


if __name__ == "__main__":
    # Example usage
    product_id = "1598534756"
    name = "iphone 17"
    quantity = 1
    price = 80000
    
    print(product_details(product_id, name, quantity, price))
