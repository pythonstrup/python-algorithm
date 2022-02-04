from bisect import bisect_right, bisect_left

def count_by_binary(arr, value):
    left_index = bisect_left(arr, value)
    right_index = bisect_right(arr, value)
    if right_index == left_index:
        return -1
    else:
        return right_index - left_index


n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(count_by_binary(arr, x))