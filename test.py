# import generate_nn
import operator
import bisect

shit = [[1, 2], [10, 1], [3, 5], [2, 2]]

by_0 = sorted(shit, key=lambda x: x[0])
by_1 = sorted(shit, key=lambda x: x[1])

print(by_0)
print(by_1)

closest_0 = bisect.bisect_left(by_0, 2, key=lambda x: x[0])
closest_1 = bisect.bisect_left(by_1, 2, key=lambda x: x[1])

print(closest_0)
print(closest_1)
