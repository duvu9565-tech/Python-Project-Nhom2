from core.node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Thêm hàng hóa vào cuối danh sách
    def append(self, hang_hoa):
        new_node = Node(hang_hoa)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Xóa theo mã hàng
    def delete_by_id(self, ma_hang):
        current = self.head

        while current is not None:

            if current.data.ma_hang == ma_hang:

                # Chỉ có 1 node
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                # Xóa đầu
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                # Xóa cuối
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Xóa giữa
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True

            current = current.next

        return False

    # Tìm theo mã hàng
    def search(self, ma_hang):

        current = self.head

        while current is not None:

            if current.data.ma_hang == ma_hang:
                return current.data

            current = current.next

        return None

    # Hiển thị từ đầu đến cuối
    def traverse_forward(self):
    current = self.head

    while current:
        print(current.data)
        print("-" * 40)
        current = current.next

    # Hiển thị ngược
    def traverse_backward(self):

        current = self.tail

        while current is not None:
            print("--------------------------------")
            print(current.data)
            current = current.prev

    # Trả về danh sách đối tượng
    def to_list(self):

        result = []

        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result

    # Kiểm tra rỗng
    def is_empty(self):
        return self.head is None

    # Đếm số lượng
    def size(self):

        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count