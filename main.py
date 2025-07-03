zakupy = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

print(zakupy)

number = 0

for shop, items_list in zakupy.items():
    capitalized_items = [item.capitalize() for item in items_list]
    items_string = ", ".join(capitalized_items)
    number += len(items_list)
    print(f"Idę do {shop.capitalize()} i kupuję tam {capitalized_items}")

print(f"W sumie kupiję {number} produktów.")

print("A tutaj wprowadzam pierwszą zmianę w kodzie :)")
