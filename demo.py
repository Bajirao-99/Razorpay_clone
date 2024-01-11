def max_special_value(N, K, arr):
    arr.sort(reverse=True)
    max_val = 0
    for i in range(N - K + 1):
        max_val = max(max_val, arr[i + K - 1])
    return max_val

N = int(input())
K = int(input())
arr = list(map(int, input().split()))

print(max_special_value(N, K, arr))
