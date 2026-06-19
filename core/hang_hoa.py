from abc import ABC, abstractmethod


class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_gia = don_gia
        self.so_luong = so_luong

    @abstractmethod
    def tinh_thanh_tien(self):
        pass

    def __str__(self):
        return (
            f"Mã hàng      : {self.ma_hang}\n"
            f"Tên hàng     : {self.ten_hang}\n"
            f"Đơn giá      : {self.don_gia}\n"
            f"Số lượng     : {self.so_luong}\n"
            f"Thành tiền   : {self.tinh_thanh_tien()}"
        )