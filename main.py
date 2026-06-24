import sys
from PySide6.QtWidgets import QApplication
from gui.QWidget import Widget
from qt_material import apply_stylesheet  # 导入美化库

if __name__ == '__main__':
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='dark_teal.xml') 
    
    widget = Widget()
    widget.show()
    sys.exit(app.exec())