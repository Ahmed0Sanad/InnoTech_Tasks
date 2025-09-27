# Extended shopping list program with insert functionality
shopping_list = [
    "Milk", "Bread", "Eggs", "Butter", "Cheese",
    "Apples", "Bananas", "Chicken", "Rice", "Pasta"
]

print("Original shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

# Insert new item
new_item = input("\nEnter item to add: ")
position = int(input("Enter position to insert (1-based): ")) - 1
shopping_list.insert(position, new_item)

print("\nUpdated shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")