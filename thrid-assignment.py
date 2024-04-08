products = {
    "1": {"name": "Laptop", "category":"Electronics", "price": 200},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

def display_category(products):
    for product_id, product_details in products.items():
        print(f"Product_ID: {product_id}, Name: {product_details['name']}, Category: {product_details['category']}")
        
def search_product(products,name):
    found = False
    for product_id, product_details in products.items():
        if product_details["name"].lower() == name.lower():
            print(f"Product '{name}' found with ID '{product_id}' in category '{product_details['category']}")
            found = True
            break
        if not found:
            print(f"Product '{name}' not found")
            
            
display_category(products)
search_product(products, "laptop")
        