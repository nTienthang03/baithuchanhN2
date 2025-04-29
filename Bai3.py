import pandas as pd

# Lớp thông tin xe
class Info_Xe:
    def __init__(self, loai_xe, chu_xe, thoi_gian, bien_so=''):
        self.loai_xe = loai_xe
        self.chu_xe = chu_xe
        self.thoi_gian = thoi_gian
        self.bien_so = bien_so

# Lớp tính tiền
class Money_Time:
    def __init__(self):
        self.gia_tien = {'Xe đạp': 2000, 'Xe máy': 5000, 'Xe điện': 3500, 'Ô tô': 10000}
        self.ds_xe = []

    def them_xe(self, xe):
        self.ds_xe.append(xe)
    def tinh_tien(self, xe):
        return self.gia_tien[xe.loai_xe] * xe.thoi_gian

    def sua_thong_tin(self, bien_so, loai_xe=None, chu_xe=None, thoi_gian=None):
        for xe in self.ds_xe:
            if xe.bien_so == bien_so:
                if loai_xe: xe.loai_xe = loai_xe
                if chu_xe: xe.chu_xe = chu_xe
                if thoi_gian: xe.thoi_gian = thoi_gian
                break

    def xoa_xe(self, bien_so):
        self.ds_xe = [xe for xe in self.ds_xe if xe.bien_so != bien_so]

    def xuat_thong_tin_tren_20k(self):
        result = []
        for xe in self.ds_xe:
            tien = self.tinh_tien(xe)
            if tien > 20000:
                result.append({
                    'Loại xe': xe.loai_xe,
                    'Chủ xe': xe.chu_xe,
                    'Thời gian gửi': xe.thoi_gian,
                    'Biển số': xe.bien_so,
                    'Thành tiền': tien
                })
        df = pd.DataFrame(result)
        df.to_excel('thong_tin_gui_xe.xlsx', index=False)
        print(df)

# Ví dụ sử dụng
nha_xe = Money_Time()
nha_xe.them_xe(Info_Xe('Xe máy', 'Nguyễn Văn A', 5, '29A-12345'))
nha_xe.them_xe(Info_Xe('Ô tô', 'Trần Thị B', 3, '30F-67890'))
nha_xe.them_xe(Info_Xe('Xe đạp', 'Lê Văn C', 12, ''))
nha_xe.them_xe(Info_Xe('Xe máy', 'Nguyễn Thị D', 20, '30A-34567'))
nha_xe.them_xe(Info_Xe('Ô tô', 'Lê Phương E', 1, '88F-23451'))

# Xuất thông tin người gửi trên 20k
nha_xe.xuat_thong_tin_tren_20k()