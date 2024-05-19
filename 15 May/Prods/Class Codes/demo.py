try:
    print(10/0)
except ArithmeticError as e:
    print("Exception Occur", e)
else:
    print("No exception occur")
print("Rest of the block")