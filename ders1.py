from PyQt6.QtWidgets import *
import sys
def özelleştir():
    dosya = open("profil_Bilgileri","w")
    dosya.write("")
    dosya.close()

    uygulama = QApplication([])
    pencere =QWidget()


    kalıp = QVBoxLayout()
    pencere.setWindowTitle("Profil")

    kalıp.addWidget(QLineEdit('Kullanızı adınız...'))
    kalıp.addWidget(QLineEdit('Şifreniz...'))
    kalıp.addWidget(QLineEdit('Mailiniz...'))

    kalıp.addWidget(QLabel('Doğum Tarihiniz'))
    kalıp.addWidget(QScrollBar())

    kalıp.addWidget(QLabel('Arka plan renginiz'))
    kalıp.addWidget(QColorDialog())

    pencere.setLayout(kalıp)

    pencere.show()

    uygulama.exec()
özelleştir()

