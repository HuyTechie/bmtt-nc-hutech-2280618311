print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")

lines = []

while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)
    
print("Dòng văn bản đã nhập sau khi chuyển thành chữ hoa: ")
for line in lines:
    print(line.upper())