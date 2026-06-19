from core.hang_hoa import HangHoa


class HangGiaDung(HangHoa):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong, chat_lieu):
        super().__init__(ma_hang, ten_hang, don_gia, so_luong)
        self.chat_lieu = chat_lieu

    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong

    def __str__(self):
        return super().__str__() + f"\nChất liệu    : {self.chat_lieu}"