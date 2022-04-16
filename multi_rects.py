import sys
# pip install pyqt5
from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QPoint, Qt
from PyQt5.QtGui import QPainter, QPixmap, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_start.clicked.connect(self.draw_rect)

        self.life = False
        # self.pix = QPixmap(self.rect().size())
        # self.pix.fill(Qt.white)
        self.begin, self.end = QPoint(), QPoint()

        self.penRectangle = None
        self.painter = None
        self.pixmap_image = None

    def draw_rect(self):
        self.life = True
        link_file = QFileDialog.getOpenFileName()
        self.pixmap_image = QPixmap(link_file[0]).scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.uic.label.setPixmap(self.pixmap_image)

    def mousePressEvent(self, event):
        if self.life:
            print('Point 1')
            self.begin = event.pos()
            self.end = self.begin

    def mouseMoveEvent(self, event):
        if self.life:
            print('Point 2')
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.life:
            print('Point 3')
            # painter = QPainter(self.pix)
            # painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            # rect = QRect(self.begin, self.end)
            # painter.drawRect(rect)

            painter = QPainter(self.pixmap_image)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(self.begin.x() - (self.width()/2-self.pixmap_image.width()/2),
                             self.begin.y(),
                             self.end.x() - self.begin.x(),
                             self.end.y() - self.begin.y())
            self.uic.label.setPixmap(self.pixmap_image)

    def paintEvent(self, event):
        painter = QPainter(self)
        # painter.drawPixmap(QPoint(), self.pix)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        rect = QRect(self.begin, self.end)
        painter.drawRect(rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
