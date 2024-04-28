from PyQt6.QtWidgets import *
import sys

uygulama = QApplication([])
pencere =QWidget()


kalıp = QVBoxLayout()

kalıp.addWidget(QPushButton('Kullanızı adınız...'))
kalıp.addWidget(QPushButton('Şifreniz...'))

pencere.setLayout(kalıp)

pencere.show()

uygulama.exec()


