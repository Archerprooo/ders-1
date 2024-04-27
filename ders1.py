from PyQt6.QtWidgets import *
import sys
aa = QApplication([])
ww =QWidget()
icerik = QVBoxLayout()
icerik.addWidget(QPushButton('tıkla'))
icerik.addWidget(QPushButton('dene'))
icerik.addWidget(QLabel('Bilgi'))
ww.setLayout(icerik)
ww.show()
aa.exec()


