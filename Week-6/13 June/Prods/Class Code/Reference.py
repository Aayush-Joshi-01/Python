import sys


y = 42
z = 42
x = 42
print(id(x))
print(id(y))
print(id(z))
ref_count = sys.getrefcount(id(x))
print("Reference count of x:", ref_count)
