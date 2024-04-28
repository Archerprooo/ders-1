from PyQt6.QtWidgets import *
import sys

uygulama = QApplication([])
pencere =QWidget()


uygulama = QVBoxLayout()

uygulama.addWidget(QPushButton('Kullanızı adınız...'))
uygulama.addWidget(QPushButton('Şifreniz...'))

pencere.setLayout(uygulama)

pencere.show()

uygulama.exec()


