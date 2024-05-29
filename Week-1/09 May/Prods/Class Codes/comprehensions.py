items = []
for val in range(1, 11):
    items.append(val * val)
print(items)

print([item * item for item in range(1, 11) if item % 2 == 0])
