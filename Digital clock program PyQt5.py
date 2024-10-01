import sys
from PyQt5.QtWidgets import (QApplication , QMainWindow , QLabel,
                             QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,
                             QPushButton)
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase
class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(600,250,200,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(140, 87%, 31%);")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("Game Of Squids.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        current = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current)

def main():
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()