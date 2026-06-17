class Node:
    def __init__(self, data=Non):
        self.data = data       # Chứa đối tượng dữ liệu hàng hóa
        self.next = None       # Con trỏ trỏ đến Node tiếp theo
        self.prev = None       # Con trỏ trỏ đến Node phía trước
