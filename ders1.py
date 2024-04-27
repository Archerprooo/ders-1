from PyQt6.QtWidgets import *
import sys

aa = QApplication([])
ww =QWidget()

icerik = QVBoxLayout()
icerik2 = QHBoxLayout()

icerik.addWidget(QPushButton('tıkla'))
icerik.addWidget(QPushButton('dene'))
icerik.addWidget(QLabel('Bilgi'))

icerik2.addWidget(QPushButton('tıkla'))
icerik2.addWidget(QPushButton('dene'))
icerik2.addWidget(QLabel('Bilgi'))


ww.setLayout(icerik)
ww.setLayout(icerik2)

ww.show()

aa.exec()


