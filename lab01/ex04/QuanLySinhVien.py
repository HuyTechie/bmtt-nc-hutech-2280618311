from sinhvien import SinhVien

class QuanLySinhVien:

    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if (self.soluongsinhvien() > 0):
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId +1

        return maxId
        

    def soluongsinhvien(self):
        return self.listSinhVien.__len__()


    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("nhap ten sinh vien: ")
        major = input("Nhap chuyen nganh của sinh vien: ")
        gender = input("nhap gioi tình sinh vien: ")
        diemTB = float(input("Nhap diem của sinh viên: "))
        sv = SinhVien(svId, name, gender, major, diemTB)

        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            gender = input("nhap giới tính sinh vien: ")
            major = input("Nhap chuyên ngành của sinh vien")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._gender = gender
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))


    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)


    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)


    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)


    def findByID(self, ID):
        searchResult = None
        if (self.soluongsinhvien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult


    def findByName(self, keyword):
        listsv = []
        if (self.soluongsinhvien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()): 
                    listsv.append(sv)
        return listsv


    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted


    def xepLoaiHocLuc(self, sv:SinhVien):

        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"
        

    def showSinhVien(self, listSV):

        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
            .format("ID", "Name", "Gender", "Major", "Diem TB", "Hoc Luc"))

        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                    .format(sv._id, sv._name, sv._gender, sv._major, sv._diemTB, sv._hocLuc))

        print("\n")


    def getListSinhVien(self):
        return self.listSinhVien