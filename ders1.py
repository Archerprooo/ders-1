from PyQt6.QtWidgets import *
import sys
class girişekranı(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        Anauygulama = QApplication([])
        Anapencere = QWidget()
        Anaekran = QVBoxLayout()
        self.anaedit1=QPushButton('özelleştir')
        self.anaedit1.setFixedWidth(100)
        Anaekran.addWidget(self.anaedit1)
        
        
        
        
        Anapencere.show()
        Anauygulama.exec()


class özelleştir(QMainWindow):
    
    def __init__(self,xx="Başlıksız"):
        
        def onayla(self):
            pencere.showFullScreen()
        def tam_ekran(self):
            pencere.showFullScreen()
        def kapat(self):
            pencere.close()

        uygulama = QApplication([])
        pencere =QWidget()
        


        kalıp = QVBoxLayout()
        pencere.setWindowTitle("Profil")

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
        
        self.buton1= QPushButton('Tamamla')
        self.buton1.setFixedWidth(100)
        kalıp.addWidget(self.buton1)
        self.buton1.clicked.connect(onayla)
        pencere.setLayout(kalıp)

        self.buton2= QPushButton('çıkış')
        self.buton2.setFixedWidth(100)
        kalıp.addWidget(self.buton2)
        self.buton2.clicked.connect(kapat)
        pencere.setLayout(kalıp)


        self.buton3= QPushButton('Tam ekran')
        self.buton3.setFixedWidth(100)
        kalıp.addWidget(self.buton3)
        self.buton3.clicked.connect(tam_ekran)
        pencere.setLayout(kalıp)
        
        pencere.show()
        uygulama.exec()


pencere = özelleştir()
Anapencere = girişekranı()


