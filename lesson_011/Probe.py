from collections import defaultdict

goods = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100],
]

good_count = defaultdict(int)
for name, quantity in goods:
    good_count[name] += quantity
print(good_count)