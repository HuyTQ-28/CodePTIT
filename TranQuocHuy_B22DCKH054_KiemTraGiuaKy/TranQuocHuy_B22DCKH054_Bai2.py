# Dynamic Programming
# Hàm lis dùng để tìm dãy không giảm dài nhất
def lis(arr):
    n = len(arr)
    dp = [1] * n

    # Duyệt chỉ số i từ 1 đến n - 1, prev từ 0 đến i - 1
    # Nếu có phần tử ở trước vị trí i mà nhỏ hơn hoặc bằng arr[i] thì dãy có thể mở rộng dãy con tới i
    # Nếu có thể mở rộng, cập nhật độ dài tại vị trí i bằng cách lấy giá trị lớn hơn
    # giữa dp[i] hiện tại và dp[prev] + 1
    for i in range(1, n):
        for prev in range(0, i):
            if arr[i] >= arr[prev]:
                dp[i] = max(dp[i], dp[prev] + 1)
    # trả về kết quả lớn nhất
    return max(dp)

a = [float(i) for i in input().split()]
print(lis(a))