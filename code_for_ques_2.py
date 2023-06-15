from itertools import combinations

nums = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
subsets = [subset for r in range(3, 7) for subset in combinations(nums, r) if sum(subset) == 0]

for subset in subsets:
    print(subset)
