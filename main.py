import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Hệ thống quản lý hàng hóa siêu thị")
window.resize(1000, 700)
window.show()

sys.exit(app.exec())