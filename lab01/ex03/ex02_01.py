def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("nhập danh sách các số, các nhau bằng dấu phẩy: ")

print("Tổng các số chẵn trong list là:", tinh_tong_so_chan(list(map(int, input_list.split(',')))))