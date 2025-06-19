def daonguoclist(lst):
    return lst[::-1]

#nhập danh sách từ người dùng avf xử lý chuỗi
input_List = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")

print("List sau khi đảo ngược là:", daonguoclist(list(map(int, input_List.split(',')))))
