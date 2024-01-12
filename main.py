import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Окружность')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_okr(qp)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_okr(self, qp):
        qp.setBrush(QColor('yellow'))
        r = random.randint(10, 300)
        qp.drawEllipse(30, 30, r + 30, r + 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
