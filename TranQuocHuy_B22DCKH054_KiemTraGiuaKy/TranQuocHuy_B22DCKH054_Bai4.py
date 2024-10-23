import matplotlib.pyplot as plt

# Lấy các từ trong đoạn văn (các từ cách nhau một khoảng trống) và lưu vào list text
text = []
while True:
    try:
        text += input().split()
    except EOFError:
        break

# Dùng dictionary word_freq để đếm tần suất xuất hiện của các từ
word_freq = {}
for word in text:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

# Lấy danh sách các từ cho vào list res và sort theo tần suất xuất hiện
res = list(word_freq.items())
res.sort(key=lambda x: x[1], reverse=True)

# Phần vẽ đồ thị
# 1. Tách từ và tần suất in ra để vẽ
words = [x[0] for x in res]
frequencies = [x[1] for x in res]

# 2. Vẽ đồ thị cột
plt.figure(figsize=(10, 6)) # thiết lập kích thước (rộng = 10, cao = 6)
plt.bar(words, frequencies, color = 'skyblue') # Vẽ biểu đồ cột (x: words, y:frequencies, color = skyblue)

# 3. Thêm tiêu đề và nhãn
plt.title('Word frequency distribution')
plt.xlabel('Word')
plt.ylabel('Frequency')

# 4. Hiển thị bằng lệnh show
plt.show()
