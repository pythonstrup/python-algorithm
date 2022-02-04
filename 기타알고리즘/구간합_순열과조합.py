
import itertools

data = [1, 2, 3, 4]

# for i in itertools.permutations(data, 2):
#     print(list(i), "=", end=" ")
#     print(sum(list(i)))

for i in itertools.combinations(data, 2):
    print(list(i), "=", end=" ")
    print(sum(list(i)))