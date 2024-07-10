def gen(num):
    for i in range(num):
        yield i


# n = gen(10)
# for i in n:
#     print(i)

def non_gen(num):
    l = []
    for i in range(num):
        l.append(i)
    return l


n = non_gen(10)
for i in n:
    print(i)
