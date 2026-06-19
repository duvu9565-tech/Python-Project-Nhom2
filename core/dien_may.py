from core.hang_hoa import HangHoa


class DienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong, bao_hanh):
        super().__init__(ma_hang, ten_hang, don_gia, so_luong)
        self.bao_hanh = bao_hanh

    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong * 1.1

    def __str__(self):
        return super().__str__() + f"\nBảo hành     : {self.bao_hanh} tháng"