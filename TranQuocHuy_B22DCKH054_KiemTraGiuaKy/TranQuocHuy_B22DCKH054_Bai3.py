# Dynamic Programming
# Mảng res lưu số chuỗi chiều dài từ 1 đến 10^5 thỏa mãn
max_N = 10**5
res = [0] * (max_N + 1)
MOD = int(1e9 + 7)

# Hàm count dùng để đếm số chuỗi chiều dài từ 1 đến 10^5 và lưu vào res
def count():
    # Khởi tạo dictionary dp với mỗi key ta sẽ có 1 list (các phần từ bằng 0)
    # dùng để đếm số chuỗi độ dài i kết thúc bằng key đó
    dp = {'a': [0] * (max_N + 1),
          'e': [0] * (max_N + 1),
          'u': [0] * (max_N + 1),
          'i': [0] * (max_N + 1),
          'o': [0] * (max_N + 1)}
    # Với độ dài bằng 1, tất cả các chuỗi kết thúc bằng 1 trong 5 nguyên âm đều bằng 1
    dp['a'][1] = dp['e'][1] = dp['u'][1] = dp['i'][1] = dp['o'][1] = 1

    # Duyệt từ 2 đến 10^5 để đếm số chuỗi độ dài i kết thúc bằng nguyên âm k (k: a, e, u, i, o)
    for i in range(2, max_N + 1):
        dp['a'][i] = dp['e'][i - 1] + dp['u'][i - 1] + dp['i'][i - 1] # do a có thể đứng sau e, u, i
        dp['e'][i] = dp['a'][i - 1] + dp['i'][i - 1] # do e có thể đứng sau a và i
        dp['u'][i] = dp['i'][i - 1] + dp['o'][i - 1] # do u có thể đứng sau i và o
        dp['i'][i] = dp['e'][i - 1] + dp['o'][i - 1] # do i có thể đứng sau e và o
        dp['o'][i] = dp['i'][i - 1] # do o có thể đứng sau i

    # kết quả đối với mỗi chuỗi độ dài idx là
    # tổng số chuỗi có độ dài i kết thúc bằng các nguyên âm a, e, u, i, a
    for idx in range(1, max_N + 1):
        res[idx] = int((dp['a'][idx] + dp['e'][idx] + dp['u'][idx] + dp['i'][idx] + dp['o'][idx]) % MOD)

count()
for t in range(int(input())):
    n = int(input())
    print(res[n])
# Bài toán này chỉ đếm được kết quả với độ dài chuỗi đến 10^5 và
# khi ta đếm các giá trị thỏa mãn trước vào res thì sẽ hiệu quả với input có nhiều testcase