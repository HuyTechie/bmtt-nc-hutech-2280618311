def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

#Dùng hàm và in kết quả
input_string = input("Mời nhập đoạn mã cần đảo ngược: ")
print("Chuỗi đã được đảo: ", dao_nguoc_chuoi(input_string))