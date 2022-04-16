import sys
# pip install pyqt5
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt, QRect, QTimer
from PyQt5.QtGui import QCursor, QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.begin = QPoint()
        self.end = QPoint()
        self.uic.Button_start.clicked.connect(self.start_cap)

        self.label = None

    def start_cap(self):
        self.setWindowOpacity(0.3)
        QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()
        print("Capture the screen...")

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(QColor("black"), 3))
        qp.setBrush(QColor(128, 128, 255, 128))
        qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.begin = event.pos()
        self.end = self.begin

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        QTimer.singleShot(1000, self.screenshot)

    def screenshot(self):
        print("screenshot")
        screen = QtGui.QGuiApplication.primaryScreen()
        window = self.windowHandle()
        if window is not None:
            screen = window.screen()
        if screen is None:
            print("failed")
            return

        original_pixmap = screen.grabWindow(0)
        output_pixmap = original_pixmap.copy(QRect(self.begin, self.end))
        output_pixmap.save("capture.png")

        self.label = QLabel(pixmap=output_pixmap)
        app.setQuitOnLastWindowClosed(True)
        self.label.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())
