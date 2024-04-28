from PyQt6.QtWidgets import *
import sys
Anauygulama = QApplication([])
Anapencere = QWidget()
Anaekran = QVBoxLayout()
class özelleştir(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        dosya = open("profil_Bilgileri","w")
        dosya.write("")
        dosya.close()

        uygulama = QApplication([])
        pencere =QWidget()


        kalıp = QVBoxLayout()
        pencere.setWindowTitle("Profil")

        kalıp.addWidget(QLineEdit('Kullanıcı adınız...'))
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

