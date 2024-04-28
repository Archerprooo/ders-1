from PyQt6.QtWidgets import *
import sys
Anauygulama = QApplication([])
Anapencere = QWidget()
Anaekran = QVBoxLayout()

class özelleştir(QMainWindow):
    def __init__(self,xx="Başlıksız"):


        uygulama = QApplication([])
        pencere =QWidget()


        kalıp = QVBoxLayout()
        pencere.setWindowTitle("Profil")

        self.edit1=QLineEdit('Kullanıcı adınız...')
        self.edit1.setFixedWidth(50)
        kalıp.addWidget(self.edit1)
        self.edit2=QLineEdit('Şifreniz...')
        kalıp.addWidget(self.edit2)
        self.edit3=QLineEdit('Mailiniz...')
        kalıp.addWidget(self.edit3)

        kalıp.addWidget(QLabel('Doğum Tarihiniz'))
        self.edit4=QScrollBar()
        kalıp.addWidget(self.edit4)

        kalıp.addWidget(QLabel('Arka plan renginiz'))
        self.edit5=QColorDialog()
        kalıp.addWidget(self.edit5)
        self.edit6= QPushButton('Tamamla')
        kalıp.addWidget(self.edit6)

        pencere.setLayout(kalıp)

        pencere.show()
        uygulama.exec()


pencere = özelleştir()


