def generator():
    for i in range(0, 3):
        yield i
        yield "ok"
map
gen = generator()
"""
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
for i in generator():
    print(i)
for i in generator():
    print(i)