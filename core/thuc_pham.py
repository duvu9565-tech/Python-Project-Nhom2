from core.hang_hoa import HangHoa


class ThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong, han_su_dung):
        super().__init__(ma_hang, ten_hang, don_gia, so_luong)
        self.han_su_dung = han_su_dung

    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong

    def __str__(self):
        return super().__str__() + f"\nHạn sử dụng  : {self.han_su_dung}"