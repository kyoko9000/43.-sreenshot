from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel

from gui import Ui_MainWindow


class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    # Mouse click event
    def mousePressEvent(self, event):
        print(" 1")
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    # Mouse movement events
    def mouseMoveEvent(self, event):
        print(" 2")
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    # Draw events
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter.drawRect(rect)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_load.clicked.connect(self.Show_pic)
        self.uic.Button_start.clicked.connect(self.draw_rect)

        self.link_file = None
        self.pixmap = None
        self.lb = None

    def Show_pic(self):
        # show picture
        self.link_file = QFileDialog.getOpenFileName()
        self.pixmap = QPixmap(self.link_file[0]).scaled(600, 400, Qt.KeepAspectRatio)
        self.uic.label.setPixmap(self.pixmap)

    def draw_rect(self):
        # show rectangle
        self.lb = MyLabel(self)  # call function of paintEvent
        self.lb.setGeometry(QRect(0, 0, 600, 400))  # limit of rectangle and set up geometry
        self.lb.setCursor(Qt.CrossCursor)  # change type of mouse cursor
        self.lb.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
