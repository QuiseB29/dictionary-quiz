resturant_menu = {
    "Starter": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course":{"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
}

user_setting = {"Steak": 17.99}
resturant_menu.update(user_setting)
print(resturant_menu)


def add_catergory(menu, category):
    if category not in menu:
        menu[category] = []
        print(f"Category '{category} added.")

def add_item(menu,category,item):
    if category in menu:
        if item not in menu[category]:
            menu[category].append(item)
            print(f"item '{item}' added to '{category}'.")
        else:
            print(f" '{item}' already exists in {category}'.")
    else:
        print(f"Category '{category}' does not exist")
        
def remove_item(menu,category,item):
    if item in menu:
        removed_count = category.pop(item)
        print(f"Item removed: '{item} - {removed_count} N/A")
    else:
        print(f"Item '{item}' is not found.")
            
        
        
add_catergory(resturant_menu, "Beverages")
add_item(resturant_menu, "Beverages", "Water, Soda")
remove_item(resturant_menu, "Bruschetta", "item")
print(resturant_menu)
