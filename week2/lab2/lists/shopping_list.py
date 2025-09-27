# Shopping list program
shopping_list = [
    "Milk", "Bread", "Eggs", "Butter", "Cheese",
    "Apples", "Bananas", "Chicken", "Rice", "Pasta"
]

print("Complete shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

print(f"\nItem 2: {shopping_list[1]}")
print(f"Item 8: {shopping_list[7]}")