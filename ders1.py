from PyQt6.QtWidgets import *
import sys
Anauygulama = QApplication([])
Anapencere = QWidget()
Anaekran = QVBoxLayout()

class özelleştir(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        def kapat(self):
            self.pencere.showFullScreen()
            print ("6")
    

        uygulama = QApplication([])
        self.pencere =QWidget()
        


        kalıp = QVBoxLayout()
        self.pencere.setWindowTitle("Profil")

        self.edit1=QLineEdit('Kullanıcı adınız...')
        self.edit1.setFixedWidth(100)
        kalıp.addWidget(self.edit1)
        self.edit2=QLineEdit('Şifreniz...')
        self.edit2.setFixedWidth(100)
        kalıp.addWidget(self.edit2)
        self.edit3=QLineEdit('Mailiniz...')
        self.edit3.setFixedWidth(100)
        kalıp.addWidget(self.edit3)

        kalıp.addWidget(QLabel('Doğum Tarihiniz'))
        self.edit4=QScrollBar()
        kalıp.addWidget(self.edit4)

        kalıp.addWidget(QLabel('Arka plan renginiz'))
        self.edit5=QColorDialog()
        kalıp.addWidget(self.edit5)
        
        self.edit6= QPushButton('Tamamla')
        self.edit6.setFixedWidth(100)
        kalıp.addWidget(self.edit6)
        self.edit6.clicked.connect(self.kapat)
        self.pencere.setLayout(kalıp)
        
        self.pencere.show()
        uygulama.exec()


pencere = özelleştir()


