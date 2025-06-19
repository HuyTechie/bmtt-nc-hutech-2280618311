def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

chuoi = input("Nhập chuỗi cần đảo ngược: ")

chuoi_dao_nguoc = dao_nguoc_chuoi(chuoi)

print(f"Chuỗi sau khi đảo ngược: {chuoi_dao_nguoc}")