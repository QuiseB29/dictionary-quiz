import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

def display_sales(sales):
    for week, data in sales.items():
        print(f"Week {week}:")
        for category, amount in data.items():
            print(f"{category}: {amount}")
        print()

def deep_copy_sales(sales, source_week, target_week):
    sales[target_week] = copy.deepcopy(sales[source_week])
    print(f"Week {target_week}'s schedule copied from Week {source_week} (Deep Copy)")

deep_copy_sales(weekly_sales, "Week 1", "Week 3")
display_sales(weekly_sales)
