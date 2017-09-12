import os

# for root, dirs, files in os.walk('../.'):
#     print(root, dirs, files)

G = os.walk('../.')
print(iter(G) is G)

L = list(G)
# print(L)

for tup in set(L):
    print(tup)
