from core.node import Node 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
      def append(self, hang_hoa):
        new_node = Node(hang_hoa)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
          def delete_by_id(self, ma_hang):
        current = self.head
        while current is not None:
            if current.data['ma_hang'] == ma_hang:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current.next = None
                current.prev = None
                return True
            current = current.next
        return False
def traverse_forward(self):
        current = self.head
        items = []
        while current is not None:
            items.append(current.data)
            current = current.next
        return items
